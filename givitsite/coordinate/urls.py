from django.urls import path

from . import views


urlpatterns = [
    path('', views.coordinator_create_view, name='coordinator_create_view'),
    path('create_brief', views.create_delivery_brief, name = 'create_delivery_brief'),   
]

