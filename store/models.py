"""Store models"""

# Django
from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    """Customer model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    """Product model"""
    name = models.CharField(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    def imageURL(self):
        """Try to solve a product image"""
        try:
            url = self.image.url
        except:
            url = "/images/placeholder.png"
        return url


class Order(models.Model):
    """Order model"""
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return str(self.transaction_id)

    def getCartItems(self):
        """Returns the total items of an order"""
        orderItems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderItems])        
        return total

    def getCartTotal(self):
        """Returns the total price of an order"""
        orderItems = self.orderitem_set.all()
        total = sum([item.getTotal() for item in orderItems])
        return total


class OrderItem(models.Model):
    """Order Item model"""
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name

    def getTotal(self):
        """Returns the item total price"""
        totalPrice = self.quantity*self.product.price
        return totalPrice


class ShippingAddress(models.Model):
    """Shipping Address model"""
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address