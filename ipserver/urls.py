from django.urls import path

from .views import get_client_ip, get_client_meta_data

urlpatterns = [
    path('', get_client_ip),
    path('meta/', get_client_meta_data),
]
