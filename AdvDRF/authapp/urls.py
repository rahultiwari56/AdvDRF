from django.urls import path
from authapp import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('stuinfo/<int:pk>', views.student_details),
    path('stuinfo/', views.student_list),
]
