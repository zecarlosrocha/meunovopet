from django.urls import path
from .views import index, doador

urlpatterns = [
    path('', index),
    path('doador', doador),
]