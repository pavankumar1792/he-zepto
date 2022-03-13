from atexit import register
from django.urls import re_path, include
from django.contrib import admin
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'coach_types', views.CoachTypeViewSet, basename='coach_types')
router.register(r'trains', views.TrainViewSet, basename='trains')
router.register(r'coaches', views.CoachViewSet, basename='coaches')

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^', include(router.urls)),
]