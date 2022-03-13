from django.test import TestCase
from rest_framework.test import APIRequestFactory

# Create your tests here.
factory = APIRequestFactory()
request = factory.post('/users', {'username': 'abc@mail.com', 'password': 'test1234', 'first_name': 'abc', 'last_name': 'def'}, format='json')