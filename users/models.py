from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class MyUser(AbstractUser):
    # add additional fields in here
    # like phone number, etc
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    is_phone_verified = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ~ {} ~ {}'.format(self.id, self.username, self.is_verified)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class PaymentMethodType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ~ {}'.format(self.id, self.name)

class PaymentMethod(models.Model):
    user = models.ForeignKey('users.MyUser', on_delete=models.CASCADE)
    payment_method_type = models.ForeignKey('PaymentMethodType', on_delete=models.CASCADE)
    is_valid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} ~ {} ~ {} ~ {}'.format(self.id, self.user, self.payment_method_type, self.is_valid)
