from django.urls import path
from authapp import views

urlpatterns = [
    path('', views.index, name='index'),
]
