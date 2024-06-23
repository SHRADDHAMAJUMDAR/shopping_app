import os
from django.shortcuts import render

from store.forms import CategoryForm, ProdForm
from .models import *
import csv
import io
from django.http import FileResponse, HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from datetime import date
#---- for messages framework ---
from django.contrib import messages


from store import utilities

# Create your views here.
def homepage(request):
    product_list = Product.objects.all()
    return render(request,'index.html', {'prod_list' : product_list})

def itemdets(request,pid):
    selected_prod=Product.objects.get(p_id=pid)
    return render(request,'itemdetail.html',{'itemdetail':selected_prod})

# =====================================================================================
#               PRODUCT
# =====================================================================================

def add_prod(request):

    if request.method == "POST":
        myform = ProdForm(data=request.POST, files=request.FILES)  # construct form object with passed data
        # myform = MenuForm(request.POST) --> for text only data 
        if myform.is_valid():
            myform.save()
            messages.info(request, 'Product added successfully')
            return redirect('/shopcart/addprod')
    else:
        myform = ProdForm()  # create a blank form
        ctx = {'my_form': myform}
        return render(request, 'product/addprod.html', ctx)
    

def show_prod(request):
    prod_list = Product.objects.all()
    return render(request, 'product/showprod.html', {'product' : prod_list})
    
    
# =====================================================================================
#               CUISINES
# =====================================================================================

def add_cat(request):

    if request.method == "POST":
        myform = CategoryForm(request.POST, request.FILES)  # construct form object with passed data
        # myform = CuisineForm(request.POST) --> for text only data 
        if myform.is_valid():
            myform.save()
            messages.info(request, 'Category added successfully')
            return redirect('/shopcart/addcat')
    else:
        myform = CategoryForm()  # create a blank form
        ctx = {'my_form': myform}
        return render(request, 'category/addcat.html', ctx)
    

def show_cat(request):
    cat_list = Category.objects.all()
    return render(request, 'category/showcat.html', {'category' : cat_list})

def edit_cat(request, cid):
    # Grab the object details which is under process
    selected_cat = Category.objects.get(cat_id = cid) # ****** where id = 1
    myform = CategoryForm(request.POST or None, request.FILES or None, instance=selected_cat)

    if request.method == "POST":
        if myform.is_valid():
            myform.save()
            messages.info(request, 'Category editted successfully')
            return redirect('show-cat')
    # present a form with data filled up
    return render(request, 'category/editcat.html', {'my_form': myform})

def delete_cat(request, cid):
    # Grab the object details which is under process
    selected_cat = Category.objects.get(cat_id = cid) # ****** where id = 1
    selected_cat.delete()
    
    # delete the image from disk
     # give path while deletion

    messages.info(request, 'Category deleted successfully')
    return redirect('show-cat')



def edit_prod(request, mid):
    # Grab the object details which is under process
    selected_menu = Product.objects.get(p_id = mid) # ****** where id = 1
    myform = ProdForm(request.POST or None, instance=selected_menu)

    if request.method == "POST":
        if myform.is_valid():
            myform.save()
            messages.info(request, 'Product editted successfully')
            return redirect('show-prod')
    # present a form with data filled up
    return render(request, 'product/editprod.html', {'my_form': myform})

def delete_prod(request, mid):
    # Grab the object details which is under process
    selected_prod = Product.objects.get(p_id = mid) # ****** where id = 1
    selected_prod.delete()
    
    os.remove(selected_prod.img.path) 

    messages.info(request, 'Product item deleted successfully')
    return redirect('show-prod')


def prodbycat(request,cid):
    select_prod=Product.objects.filter(p_cat=cid) #get all the menu items for the selected cuisine
    select_cat=Category.objects.get(cat_id=cid)#get the selected cuisine details
    return render(request,'product/showprodbycat.html',{ 'prodlist':select_prod, 'category':select_cat})

# def search_results(request):
#     query = request.GET.get('q')

#     if query:
#         results = MenuItem.objects.filter(name__icontains=query)
        
#     else:
#         results = []

#     return render(request, 'menu/search_results.html', {'results': results, 'query': query})