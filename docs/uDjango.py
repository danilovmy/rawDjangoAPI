# https://github.com/danilovmy/uDjango
from django import urls, http
from django.core.asgi import ASGIHandler as app

async def hello_world(*args, **kwargs):
    return http.JsonResponse({'Hello': 'World!'})

ROOT_URLCONF = urls.path('', hello_world, name='index'),
