from django.urls import path

from . import views

urlpatterns = [
    path('request', views.itemRequest_create_view, name = 'itemRequest_create_view'),
    path('feed', views.requestItem, name = 'requestItem'),
]
