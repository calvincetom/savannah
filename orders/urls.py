from rest_framework.routers import DefaultRouter
from orders.views import CustomerViewSet, OrderViewSet
from django.urls import path, include

# bind routes
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    # OIDC URLs
    path('oidc/', include('mozilla_django_oidc.urls')),
] + router.urls 