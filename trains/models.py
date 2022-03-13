from cProfile import run
from tabnanny import verbose
from django.db import models

# Create your models here.
class CoachType(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    seats = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} ~ {} ~ {}'.format(self.name, self.price, self.seats)


class Train(models.Model):
    name = models.CharField(max_length=100)
    number = models.IntegerField()
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    departure_time = models.TimeField()
    runs_on_sunday = models.BooleanField(default=False)
    runs_on_monday = models.BooleanField(default=False)
    runs_on_tuesday = models.BooleanField(default=False)
    runs_on_wednesday = models.BooleanField(default=False)
    runs_on_thursday = models.BooleanField(default=False)
    runs_on_friday = models.BooleanField(default=False)
    runs_on_saturday = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} ~ {} ~ {} ~ {}'.format(self.name, self.number, self.source, self.destination)

class Coach(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    coach_type = models.ForeignKey(CoachType, on_delete=models.CASCADE)
    coach_number = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return '{} ~ {}'.format(self.train, self.coach_type)

    class Meta:
        verbose_name_plural = 'Coaches'
