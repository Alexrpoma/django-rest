from rest_framework import routers
from .api import CustomerViewSet, AddressViewSet

router = routers.DefaultRouter()

router.register('api/customer', CustomerViewSet, 'customer')
router.register('api/address', AddressViewSet, 'address')

urlpatterns = router.urls