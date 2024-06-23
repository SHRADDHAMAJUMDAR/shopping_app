from django.http import JsonResponse
from django.shortcuts import render

from cartops.cart import Cart

# Create your views here.

def cart_add(request):
    if request.method=="POST":
        prodid=request.POST["pid"]
        prodqty=request.POST["pqty"]
        mycart=Cart(request) #get instance of existing cart
        mycart.add_item(prod_id=prodid,prod_qty=prodqty)
        cart_qty=len(mycart) #get no. of items in the cart
        response=JsonResponse({"qty":cart_qty}) #create a json response for the quantity in ajax call
        return response
    

def cartsum(request):
    mycart=Cart(request)
    prodlist=mycart.getprodlist()
    prodqty=mycart.getprodqty()
    cart_tot=mycart.totalprice()


    return render(request,'cartsummary.html',{"cart_products":prodlist,"cart_prodqty":prodqty,"cart_total":cart_tot})   

def cartupd(request):
     if request.method=="POST":
        prodid=request.POST["pid"]
        prodqty=request.POST["pqty"]
        mycart=Cart(request)
        mycart.updateprodqty(prodid,prodqty)
        prodqty=len(mycart)
        cart_tot=mycart.totalprice()
        response=JsonResponse({"qty":prodqty,"tot":cart_tot}) #create a json response for the quantity in ajax call
        return response
     

def cartdelete(request):
     if request.method=="POST":
        prodid=request.POST["pid"]
        
        mycart=Cart(request)
        mycart.delcart(prodid)
        prodqty=len(mycart)
        cart_tot=mycart.totalprice()
        response=JsonResponse({"qty":prodqty,"tot":cart_tot})
        return response




    


    


