from pyexpat import model
from django.shortcuts import render
from rest_framework import viewsets
from .models import MyUser, PaymentMethodType, PaymentMethod
from .serializers import MyUserSerializer, PaymentMethodSerializer, PaymentMethodTypeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.contrib.auth import authenticate, login, logout
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authtoken.models import Token


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the users index.")


class MyUserView(viewsets.ModelViewSet):
    serializer_class = MyUserSerializer
    model = MyUser
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.is_superuser:
            return MyUser.objects.all()
        elif user.is_authenticated:
            return MyUser.objects.filter(id=user.id)
        else:
            raise PermissionDenied('You are not authenticated')
            # return MyUser.objects.none()


class PaymentMethodView(viewsets.ModelViewSet):
    serializer_class = PaymentMethodSerializer
    model = PaymentMethod
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return PaymentMethod.objects.filter(user=user)
        else:
            raise PermissionDenied('You are not authenticated')


class PaymentMethodTypeView(viewsets.ModelViewSet):
    serializer_class = PaymentMethodTypeSerializer
    model = PaymentMethodType
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and (user.is_staff or user.is_superuser):
            return PaymentMethodType.objects.all()
        elif user.is_authenticated:
            raise PermissionDenied('You are not allowed to view this page')
        else:
            raise PermissionDenied('You are not authenticated')


def login(request):
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    if username is None or password is None:
        return HttpResponseBadRequest('Missing username or password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        token = Token.objects.get_or_create(user=user)
        return JsonResponse({'token' : token[0].key, 'username': token[0].user.username}, status=200)
    else:
        return HttpResponseBadRequest('Invalid credentials')
