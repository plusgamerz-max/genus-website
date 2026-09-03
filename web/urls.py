from django.contrib import admin
from django.urls import path, include
from django.conf import settings

import app.urls
import demo.urls

# Pages only up when DEBUG=True
debug_urlpatterns = [
    # Admin Page
    path('admin/', admin.site.urls),

    # Pages
    path('demo/', include(demo.urls))
]

urlpatterns = [
    # Pages
    path('', include(app.urls))
]

if settings.DEBUG:
    for item in debug_urlpatterns:
        urlpatterns.append(item)