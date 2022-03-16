"""Store Views"""

# Django
from django.shortcuts import render
# Models
from .models import *


def store(request):
    """Store view"""

    products = Product.objects.all()
    context = {'products': products}
    return render(
        request=request,
        template_name='store/store.html',
        context=context
    )
    

def cart(request):
    """Cart view"""

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {
            'getCartItems': 0,
            'getCartTotal': 0
        }
    
    context = {
        'items': items,
        'order': order
    }
    return render(
        request=request,
        template_name='store/cart.html',
        context=context
    )


def checkout(request):
    """Checkout view"""

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()

    else:
        items = []
        order = {
            'getCartItems': 0,
            'getCartTotal': 0
        }

    context = {
        'items': items,
        'order': order
    }
    return render(
        request=request,
        template_name='store/checkout.html',
        context=context
    )