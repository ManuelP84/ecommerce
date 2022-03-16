"""Store URLs"""

# Django
from django.urls import path

# Views
from . import views as store_views


urlpatterns = [
    path(
        route='store/',
        view=store_views.store,
        name='store' 
    ),

    path(
        route='cart/',
        view=store_views.cart,
        name='cart' 
    ),

    path(
        route='checkout/',
        view=store_views.checkout,
        name='checkout' 
    ),
]