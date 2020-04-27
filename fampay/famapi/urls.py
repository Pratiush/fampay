from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import routers

router = DefaultRouter()
router.register(r'videos', views.VideoViewSet)

urlpatterns = [
    path('ping/', views.healthCheck, name='ping'),
    path('',include(router.urls)),
    path('task/',views.backgroundTask,name='task')
]