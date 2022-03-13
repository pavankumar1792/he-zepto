from posixpath import basename
from rest_framework import routers
from django.contrib import admin
from . import views
from django.urls import re_path, include


router = routers.DefaultRouter()
router.register(r'users', views.MyUserView, basename='users')
router.register(r'paymentmethods', views.PaymentMethodView, basename='paymentmethods')
router.register(r'paymentmethodtypes', views.PaymentMethodTypeView, basename='paymentmethodtypes')
# admin.autodisover()

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^', include(router.urls)),
    re_path(r'^login', views.login, name='login'),
]