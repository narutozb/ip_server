from django.urls import path

from .views import get_client_ip

urlpatterns = [
    path('', get_client_ip)
]
