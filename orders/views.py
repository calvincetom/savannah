"""import settings for africastalking initialization"""
import africastalking

# import phone number for international formating
from phonenumbers import format_number, PhoneNumberFormat
from django.conf import settings
from rest_framework import viewsets, permissions
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
from orders.models import Customer, Order
from orders.serializers import CustomerSerializer, OrderSerializer


# Initialize Africastalking Api
africastalking.initialize(
    settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY
)
SMS = africastalking.SMS


class CustomerViewSet(viewsets.ModelViewSet):
    """Customer Viewset"""

    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """order viewset"""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer
        # Format phone number to international format
        phone_number_international = format_number(
            customer.phone_number, PhoneNumberFormat.E164
        )
        message = f" Hi {customer.name}, your order for {order.item} of amount {order.amount}, has been placed successfully."
        print(f"sending SMS to {phone_number_international}")
        SMS.send(message, [phone_number_international])  # send sms

class LogoutView(View):
    """Logout custom view"""
    def post(self, request, *args, **kwargs):
        """ Clear the user session if authenticated"""
        if request.user.is_authenticated:
            logout(request)

        # Redirect to Auth0 logout URL
        client_id = '3WejaIcVvmmGaRmTuqsLnEA835SlhMPS'
        auth0_domain = 'dev-77rk2zmat13ucvt2.uk.auth0.com'  # e.g., your-tenant.auth0.com
        return HttpResponseRedirect(f'https://{auth0_domain}/v2/logout?returnTo={reverse("login")}&client_id={client_id}')
    