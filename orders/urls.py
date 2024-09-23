"""Rest API modules"""
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from orders.views import CustomerViewSet, OrderViewSet, LogoutView

# bind routes
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    # OIDC URLs
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('oidc/', include('mozilla_django_oidc.urls')),
] + router.urls
