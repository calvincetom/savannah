"""imports for os and africastalking"""
import os
import africastalking

# import phone number for international formating
from phonenumbers import format_number, PhoneNumberFormat

from django.shortcuts import redirect
from django.contrib.auth import logout
from django.views import View
from django.http import HttpResponseRedirect

from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse


from dotenv import load_dotenv

from orders.models import Customer, Order
from orders.serializers import CustomerSerializer, OrderSerializer


# Load environment variables from .env file
load_dotenv()

# Initialize Africa's Talking with environment variables
africastalking.initialize(
    os.environ.get('AFRICASTALKING_USERNAME'),
    os.environ.get('AFRICASTALKING_API_KEY')
)
SMS = africastalking.SMS


class CustomApiRootView(APIView):
    """Custom API Root View to redirect unauthenticated users."""

    def get(self, request, *args, **kwargs):
        """Get request Method"""
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')  # Change to your signup URL if needed
        
        # If authenticated, return the default API root response
        return Response({
            'customers': reverse('customer-list', request=request),
            'orders': reverse('order-list', request=request),
        })


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
    """Logout custom view."""
    def post(self, request, *args, **kwargs):
        """Clear the user session if authenticated."""
        if request.user.is_authenticated:
            logout(request)

        # Redirect to Auth0 logout URL
        client_id = '3WejaIcVvmmGaRmTuqsLnEA835SlhMPS'
        auth0_domain = 'dev-77rk2zmat13ucvt2.uk.auth0.com'
        return_to_url = 'https://savannah-ctrg.onrender.com/accounts/login/'
        return HttpResponseRedirect(
            f'https://{auth0_domain}/v2/logout?returnTo={return_to_url}&client_id={client_id}'
        )
    