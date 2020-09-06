from django.urls import path

from . import views


urlpatterns = [
    path('', views.coordinator_create_view, name='coordinator_create_view'),
    path('file', views.create_file, name = 'create_file'),
    path('test', views.test, name = 'test'),
]
