from django.urls import path
from . import views
from .views import aircrew_detail

urlpatterns = [
    path('<int:pk>/', aircrew_detail, name='aircrew_detail'),
]
