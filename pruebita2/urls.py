from django.urls import path
from . import views

urlpatterns = [
    path('pruebita2/', views.muestra_datos, name='pruebita2'),
]