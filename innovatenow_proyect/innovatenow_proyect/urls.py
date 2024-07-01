from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quienes-somos/', views.quienes_somos, name='quienes_somos'),
    path('servicios/', views.servicios, name='servicios'),
]