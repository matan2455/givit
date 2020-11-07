from django.urls import path

from . import views

urlpatterns = [
    path('', views.coordinator_create_view, name='coordinator_create_view'),
    path('brief', views.render_coordinated_items,
         name='render_coordinated_items')
]
