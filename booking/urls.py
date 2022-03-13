from django import views
from rest_framework import routers
from django.urls import re_path, include
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^', include(router.urls)),
    re_path(r'^search_trains/', views.search_trains, name='search_trains'),
    re_path(r'^list_available_coaches/', views.list_available_coaches, name='list_available_coaches'),
    re_path(r'^list_available_berths/', views.list_available_berths, name='list_available_berths'),
]