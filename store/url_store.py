from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('home/', homepage,name='home'),
    path('', homepage,name='home'),
    path('itemdets/<int:pid>', itemdets,name='itemdets'),

        # -------- category ------
    path('addcat/', views.add_cat, name='add-cat'),
    path('showcat/', views.show_cat, name='show-cat'),
    path('editcat/<int:cid>/', views.edit_cat, name='cat-edit'),
    path('deletecat/<int:cid>/', views.delete_cat, name='cat-delete'),
#------menu------------
    path('addprod/', views.add_prod, name='add-prod'),
    path('showprod/', views.show_prod, name='show-prod'),
    path('editprod/<int:mid>/', views.edit_prod, name='prod-edit'),
    path('deleteprod/<int:mid>/', views.delete_prod, name='prod-delete'),
    path('showprodbycat/<int:cid>/', views.prodbycat, name='prod-by-cat'),

   

]
