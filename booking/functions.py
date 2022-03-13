from trains.models import Train, Coach, CoachType
from users.models import MyUser, PaymentMethod, PaymentMethodType
from .models import Booking, BookingDetail, Payment
import datetime
import calendar


def get_available_trains(from_station, to_station, date, coach_type):
    # print(date.weekday())
    # print(calendar.day_name[date.weekday()])
    if calendar.day_name[date.weekday()] == 'Monday':
        trains = Train.objects.filter(source=from_station, destination=to_station, runs_on_monday=True)
    elif calendar.day_name[date.weekday()] == 'Tuesday':
        trains = Train.objects.filter(source=from_station, destination=to_station, runs_on_tuesday=True)
    elif calendar.day_name[date.weekday()] == 'Wednesday':
        trains = Train.objects.filter(source=from_station, destination=to_station, runs_on_wednesday=True)
    elif calendar.day_name[date.weekday()] == 'Thursday':
        trains = Train.objects.filter(source=from_station, destination=to_station, runs_on_thursday=True)
    elif calendar.day_name[date.weekday()] == 'Friday':
        trains = Train.objects.filter(source=from_station, destination=to_station, runs_on_friday=True)
    elif calendar.day_name[date.weekday()] == 'Saturday':
        trains = Train.objects.filter(source=from_station, destination=to_station, runs_on_saturday=True)
    elif calendar.day_name[date.weekday()] == 'Sunday':
        trains = Train.objects.filter(source=from_station, destination=to_station, runs_on_sunday=True)
    else:
        trains = Train.objects.filter(source=from_station, destination=to_station)

    if coach_type is not None:
        coach_type = CoachType.objects.filter(id__in=coach_type)
        trains = trains.filter(coach__coach_type=coach_type)
    # print(trains.count())
    # print(trains)
    return trains.values('id', 'name', 'number', 'source', 'destination', 'arrival_time', 'departure_time')


def get_available_coaches(train_number, date, coach_type):
    # print(train_number)
    train = Train.objects.get(number=train_number)
    coaches = Coach.objects.filter(train__number=train_number)
    if coach_type is not None:
        coaches = coaches.filter(coach_type__id__in=coach_type)
    coach_availability = {}
    for coach in coaches:
        booked = BookingDetail.objects.filter(booking__train=train, booking__date=date, coach=coach, booking__status__in=[1,4]).count()
        coach_availability[coach.coach_number] = coach.coach_type.seats - booked
    return coach_availability


def get_available_berths(train_number, date, coach_number):
    train = Train.objects.get(number=train_number)
    coach = Coach.objects.get(train=train, coach_number=coach_number)
    booked = BookingDetail.objects.filter(booking__train=train, booking__date=date, coach=coach, booking__status__in=[1,4]).values_list('seat_number', flat=True)
    seats = [i for i in range(1, coach.coach_type.seats+1)]
    available_seats = list(set(seats) - set(booked))
    return available_seats


def make_booking(user, train_number, date, coach_number, customer_details, berth_numbers, payment_method):
    train = Train.objects.get(number=train_number)
    coach = Coach.objects.get(train=train, coach_number=coach_number)
    # payment_method = PaymentMethod.objects.get(id=payment_method)
    booking = Booking.objects.create(user=user, train=train, date=date, status=4) # pending status
    if berth_numbers is None:
        train = Train.objects.get(number=train_number)
        coach = Coach.objects.get(train=train, coach_number=coach_number)
        booked = BookingDetail.objects.filter(booking__train=train, booking__date=date, coach=coach, booking__status__in=[1,4]).values_list('seat_number', flat=True)
        seats = [i for i in range(1, coach.coach_type.seats+1)]
        available_seats = list(set(seats) - set(booked))
        berth_numbers = available_seats[:len(customer_details)+1]
    bookings = []
    amount = 0
    for customer, berth_number in zip(customer_details, berth_numbers):
        b = BookingDetail(booking=booking, coach=coach, seat_number=berth_number, name=customer.name, age=customer.age)
        amount += coach.coach_type.fare
        booking.append(b)
    BookingDetail.objects.bulk_create(bookings, batch_size=100)
    payment = Payment.objects.create(user=user, booking=booking, payment_method=payment_method, amount=amount)
    return payment.values('id', 'booking_id', 'payment_method_id', 'amount')
