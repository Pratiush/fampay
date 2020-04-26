from django.urls import path, include
from . import views


urlpatterns = [
    path('ping/', views.healthCheck, name='ping'),
]