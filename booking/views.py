from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
import datetime
import calendar
from .functions import get_available_berths, get_available_trains, get_available_coaches, make_booking

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the booking index.")


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def search_trains(request):
    # print(request.data)
    source = request.data.get('source', None)
    destination = request.data.get('destination', None)
    date = request.data.get('date', None)
    coach_type = request.data.get('coach_type', None)
    if source is None:
        return HttpResponseBadRequest('Please provide source')
    if destination is None:
        return HttpResponseBadRequest('Please provide destination')
    if date is None:
        return HttpResponseBadRequest('Please provide date')
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    trains = get_available_trains(source.upper(), destination.upper(), date, coach_type)
    return JsonResponse(list(trains), safe=False, status=200)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def list_available_coaches(request):
    # print(request.data)
    train_number = request.data.get('train_number', None)
    date = request.data.get('date', None)
    coach_type = request.data.get('coach_type', None)
    if train_number is None:
        return HttpResponseBadRequest('Please provide train number')
    if date is None:
        return HttpResponseBadRequest('Please provide date')
    coaches_available = get_available_coaches(train_number, date, coach_type)
    return JsonResponse(coaches_available, safe=False, status=200)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def list_available_berths(request):
    print(request.data)
    train_number = request.data.get('train_number', None)
    date = request.data.get('date', None)
    coach_number = request.data.get('coach_number', None)
    if train_number is None:
        return HttpResponseBadRequest('Please provide train number')
    if date is None:
        return HttpResponseBadRequest('Please provide date')
    if coach_number is None:
        return HttpResponseBadRequest('Please provide coach number')
    berths_available = get_available_berths(train_number, date, coach_number)
    return JsonResponse(berths_available, safe=False, status=200)


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
@csrf_exempt
def book_ticket(request):
    # print(request.data)
    train_number = request.data.get('train_number', None)
    date = request.data.get('date', None)
    coach_number = request.data.get('coach_number', None)
    customer_details = request.data.get('customer_details', None)
    berth_numbers = request.data.get('berth_numbers', None)
    if train_number is None:
        return HttpResponseBadRequest('Please provide train number')
    if date is None:
        return HttpResponseBadRequest('Please provide date')
    if coach_number is None:
        return HttpResponseBadRequest('Please provide coach number')
    if customer_details is None:
        return HttpResponseBadRequest('Please provide customer details')
    if berth_numbers is not None and len(berth_numbers) != len(customer_details):
        return HttpResponseBadRequest('Customer details and selected berth numbers mismatch')
    for customer in customer_details:
        if 'name' not in customer or 'age' not in customer:
            return HttpResponseBadRequest('All Customer details must contain name and age')
    payment = make_booking(request.user, train_number, date, coach_number, customer_details, berth_numbers)
    return JsonResponse(payment, safe=False, status=200)

def list_bookings(request):
    return HttpResponse("Returns logged in user's bookings list.")

def cancel_booking(request):
    return HttpResponse("Cancels a logged in user's booking.")

def get_booking_details(request):
    return render(request, 'booking/get_booking_details.html')
