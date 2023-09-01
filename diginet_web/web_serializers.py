from rest_framework import serializers
from .models import Customer, Address


class AddressSerializer(serializers.ModelSerializer):
  class Meta:
    model = Address
    fields = ('uuid', 'street', 'city', 'country')

class CustomerSerializer(serializers.ModelSerializer):
  address = AddressSerializer()
  class Meta:
    model = Customer
    fields = ('uuid', 'username', 'fullname', 'email', 'address', 'created_at')
    read_only_fields = ('created_at',)
  
  def create(self, validated_data):
        address_data = validated_data.pop('address')
        address, created = Address.objects.get_or_create(**address_data)
        customer = Customer.objects.create(address=address, **validated_data)
        return customer
