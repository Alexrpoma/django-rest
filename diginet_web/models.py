from django.db import models
from uuid import uuid4

# Create your models here.

class Address(models.Model):
  uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  street = models.CharField(max_length=25)
  city = models.CharField(max_length=25)
  country = models.CharField(max_length=30)

  def __str__(self) -> str:
    return f'(Street: {self.street} City: {self.city} Country: {self.country})'

class Customer(models.Model):
  uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  username = models.CharField(max_length=10)
  fullname = models.CharField(max_length=30)
  email = models.CharField(max_length=25, unique=True)
  address = models.ForeignKey(Address, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self) -> str:
    return f'(Username: {self.username} Fullname: {self.fullname} email: {self.email} address: {self.address} created_at: {self.created_at})'