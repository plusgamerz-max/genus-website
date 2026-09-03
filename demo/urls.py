from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path('textarea', views.textarea_demo, name='textarea demo')
]