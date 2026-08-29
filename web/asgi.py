import colorama
colorama.init(wrap=True, strip=False, convert=True)

import os

''' Use it to update settings module name'''
os.environ.update({
    'DJANGO_SETTINGS_MODULE': 'web.settings',
    'DJANGO_ALLOW_ASYNC_UNSAFE': 'true',
})

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web.settings')

from django.core.asgi import get_asgi_application
django_app = get_asgi_application()

from starlette.applications import Starlette
from starlette.routing import Mount

from api.main import app as api_app

app = Starlette(routes=[
    Mount("/api/v1", app=api_app),   # fastapi route
    Mount("/", app=django_app),     # django and all other app route
])