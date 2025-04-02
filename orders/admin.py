from django.contrib import admin
from orders.models import Customer, Order
# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)