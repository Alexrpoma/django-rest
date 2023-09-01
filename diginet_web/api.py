from .models import Customer, Address
from rest_framework import viewsets, permissions
from .web_serializers import CustomerSerializer, AddressSerializer

class CustomerViewSet(viewsets.ModelViewSet):
  queryset = Customer.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = CustomerSerializer


class AddressViewSet(viewsets.ModelViewSet):
  queryset = Address.objects.all()
  permission_classes = [permissions.AllowAny]
  serializer_class = AddressSerializer