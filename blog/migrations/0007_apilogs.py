# Generated by Django 3.0 on 2021-12-10 06:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20211122_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiLogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='', max_length=10000)),
                ('method', models.CharField(default='', max_length=10)),
                ('host', models.CharField(default='', max_length=100)),
                ('query_parameters', django.contrib.postgres.fields.jsonb.JSONField(default={})),
                ('username', models.CharField(default='', max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
