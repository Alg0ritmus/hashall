from django.urls import path
from . import views

app_name = 'hashit'

urlpatterns = [
    path('', views.index, name='index'),
    path('hash/', views.get_hash, name='get_hash'),
]