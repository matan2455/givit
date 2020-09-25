from django.urls import path

from . import views

urlpatterns = [
    path('', views.coordinator_create_view, name='coordinator_create_view'),
    path('filter_requests', views.filter_coordinator_view, name='filter_coordinator_view')  
    
]
