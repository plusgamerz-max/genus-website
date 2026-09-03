from django.urls import path
from . import views

urlpatterns = [
    # Favicon Icon
    path('favicon.ico', views.favicon_ico),

    # Pages
    path('home', views.home, name='home'),
    path('proto', views.proto, name='prototype')
]