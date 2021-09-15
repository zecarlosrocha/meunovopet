from django.urls import path
from .views import index, doador, animal

urlpatterns = [
    path('', index,name='index'),
    path('doador', doador, name='doador'),
    path('animal/<int:pk>', animal, name='animal'),
]