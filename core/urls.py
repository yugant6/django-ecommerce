from django.urls import path
from .views import ItemDetailView
from .views import CheckoutView
from .views import HomeView
from .views import add_cart
from .views import remove_single_cart
from .views import remove_cart
from .views import add_single_cart
from .views import OrderSummaryView



app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('add-cart/<slug>/', add_cart, name='add-cart'),
    path('remove-cart/<slug>/', remove_cart, name='remove-cart'),
    path('add-single-cart/<slug>', add_single_cart, name='add-single-cart'),
    path('remove-single-cart/<slug>/',
         remove_single_cart, name='remove-single-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary')


]
