from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Train, Coach, CoachType
from .serializers import TrainSerializer, CoachSerializer, CoachTypeSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponse
from rest_framework.exceptions import ValidationError


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the trains index.")

class CoachTypeViewSet(viewsets.ModelViewSet):
    model = CoachType
    serializer_class = CoachTypeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and (user.is_staff or user.is_superuser):
            return CoachType.objects.all()
            return CoachType.objects.all()
        elif user.is_authenticated:
            raise PermissionError('You are not allowed to view this page')
        else:
            raise PermissionError('You are not authenticated')


class TrainViewSet(viewsets.ModelViewSet):
    model = Train
    serializer_class = TrainSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and (user.is_staff or user.is_superuser):
            return Train.objects.all()
        elif user.is_authenticated:
            raise PermissionError('You are not allowed to view this page')
        else:
            raise PermissionError('You are not authenticated')


class CoachViewSet(viewsets.ModelViewSet):
    model = Coach
    serializer_class = CoachSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        # train_id = self.request.query_params.get('train_id', None)
        # if train_id is None:
        #     raise ValidationError("Provide train_id as url parameter.")
        if user.is_authenticated and (user.is_staff or user.is_superuser):
            return Coach.objects.all()
        elif user.is_authenticated:
            raise PermissionError('You are not allowed to view this page')
        else:
            raise PermissionError('You are not authenticated')