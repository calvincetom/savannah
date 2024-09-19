"""import settings for africastalking initialization"""
import africastalking

# import phone number for international formating
from phonenumbers import format_number, PhoneNumberFormat
from django.conf import settings
from rest_framework import viewsets, permissions
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
