from django.urls import path

from .views import aircraft_detail

urlpatterns = [
    path('<int:pk>/', aircraft_detail, name='aircraft_detail'),
]
