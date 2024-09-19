"""Modules to map model objects"""
from rest_framework import serializers
from .models import Customer, Order

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer objects"""
    class Meta:
        """Meta class for Customer Model"""
        model = Customer
        fields = ['id', 'name','phone_number', 'code']

class OrderSerializer(serializers.ModelSerializer):
    """Serializer for Customer objects"""

    class Meta:
        """Meta class for Customer Model"""
        model = Order
        fields = ['id', 'customer', 'item', 'amount', 'time']

    def validate_amount(self, value):
        """Validate the amount value entered"""
        if value < 0:
            raise serializers.ValidationError('Amount entered cannot be negative.')
        return value