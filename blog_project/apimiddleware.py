from blog.models import *


def APiLogMiddleware(get_response):
    def process_request(request):
        response = get_response(request)
        print(request.META, "")
        api_log = ApiLogs(url=request.path,
                          method=request.META['REQUEST_METHOD'],
                          host=request.META['HTTP_HOST'],
                          query_parameters=dict(request.GET),
                          username=request.user,

                          )
        api_log.save()
        return response

    return process_request
