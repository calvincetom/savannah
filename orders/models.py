"""Modules providing database modelling"""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Customer model.
class Customer(models.Model):
    """Class representing a customer"""

    name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(blank=False, region="KE")
    code = models.CharField(max_length=100, unique=True)

    def __str__(self) -> object:
        return f"{self.name}"


# Order model
class Order(models.Model):
    """Class representing an Order"""

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    item = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> object:
        return f"{self.item} - {self.customer.name}"
