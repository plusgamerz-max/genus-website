from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.http import FileResponse, Http404
import os

# Favicon Icon
def favicon_ico(_):
    BASE_DIR = settings.BASE_DIR
    file_path = BASE_DIR / "static" / "favicon.ico"
    if os.path.isfile(file_path):
        file_data = open(file_path, 'rb')
        return FileResponse(file_data, content_type="image/png")
    raise Http404("favicon.ico doesn't exist!")

# Pages
def home(_):
    return HttpResponse("Hello!")