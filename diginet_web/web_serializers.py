from rest_framework import serializers
from .models import Customer, Address

class CustomerSerializer(serializers.ModelSerializer):
  class Meta:
    model = Customer
    fields = ('uuid', 'username', 'fullname', 'email', 'address', 'created_at')
    read_only_fields = ('created_at',)

class AddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = Address
    fields = ('uuid', 'street', 'city', 'country')