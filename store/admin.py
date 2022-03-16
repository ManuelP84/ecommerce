"""Admin"""

# Django
from django.contrib import admin
# Models
from .models import *


admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


