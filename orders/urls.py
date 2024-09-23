"""Rest API modules"""
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from orders.views import CustomerViewSet, OrderViewSet, LogoutView, CustomApiRootView

# bind routes
router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', CustomApiRootView.as_view(), name='api-root'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    # OIDC URLs
    path('oidc/', include('mozilla_django_oidc.urls')),
] + router.urls
