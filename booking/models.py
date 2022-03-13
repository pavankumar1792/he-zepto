from django.db import models
from .choices import *

# Create your models here.
class Booking(models.Model):
    user = models.ForeignKey('users.MyUser', on_delete=models.CASCADE)
    train = models.ForeignKey('trains.Train', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.IntegerField(choices=BookingStatus.choices(), default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} ~ {} ~ {} ~ {}'.format(self.id, self.user, self.train, self.date)


class BookingDetail(models.Model):
    booking = models.ForeignKey('booking.Booking', on_delete=models.CASCADE)
    coach = models.ForeignKey('trains.Coach', on_delete=models.CASCADE)
    coach_type = models.ForeignKey('trains.CoachType', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    seat_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ~ {} ~ {} ~ {} ~ {}'.format(self.id, self.booking, self.coach, self.coach_type, self.seat_number)


class Payment(models.Model):
    user = models.ForeignKey('users.MyUser', on_delete=models.CASCADE)
    booking = models.ForeignKey('booking.Booking', on_delete=models.CASCADE)
    payment_method = models.ForeignKey('users.PaymentMethod', on_delete=models.CASCADE, blank=True, null=True)
    amount = models.FloatField(default=0)
    is_payment_pending = models.BooleanField(default=True)
    is_payment_success = models.BooleanField(default=False)
    is_refund_complete = models.BooleanField(default=False)
    is_refund_initated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ~ {} ~ {} ~ {} ~ {} ~ {}'.format(self.id, self.user, self.booking, self.payment_method, self.amount, self.status)