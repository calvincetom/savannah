from rest_framework import viewsets, permissions
from orders.models import Customer, Order
from orders.serializers import CustomerSerializer, OrderSerializer

#import phone number for international formating
from phonenumbers import format_number, PhoneNumberFormat

# import settings for africastalking initialization
import africastalking
from django.conf import settings

#Initialize Africastalking Api
africastalking.initialize(settings.AFRICASTALKING_USERNAME, settings.AFRICASTALKING_API_KEY)
sms = africastalking.SMS

# Customer Viewset
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]

# order viewset
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


    def perform_create(self, serializer):
        order = serializer.save()
        customer = order.customer
        # Format phone number to international format
        phone_number_international = format_number(customer.phone_number, PhoneNumberFormat.E164)
        message  = f" Hi {customer.name}, your order for {order.item}, has been placed successfully."
        print(f'sending SMS to {phone_number_international}')
        sms.send(message, [phone_number_international]) # send sms