from .views import *
from django.urls import path


urlpatterns = [
    path('addcart/', cart_add,name='addcart'),
    path('cartsummary/', cartsum,name='cartsum'),
    path('cartupdate/', cartupd,name='cartupdate'),
    path('cartdel/', cartdelete,name='cartdel'),

   
   

]
