import json
import os
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
# ------ for authentication -----------
from django.contrib.auth import authenticate, login, logout

from cartops.cart import Cart
from store.models import UserProfile

# ------ for menu forms -------------
#from .forms import MenuForm

# ------ for custom user forms -------------
#from .forms import CuisineForm
#from .models import MenuItem

# ------ models ----
from .models import *
#from home.models import Feedback

# =====================================================================================
#               AUTHENTICATION
# =====================================================================================

def signup_page(request):

    if request.method == "POST":
        uname = request.POST['txtUname']
        fname = request.POST['txtFname']
        lname = request.POST['txtLname']
        umail= request.POST['txtEmail']
        upass = request.POST['txtPass']
        uconfpass = request.POST['txtConfPass']


        myuser=User.objects.create_user(uname,umail,upass)
        myuser.first_name=fname
        myuser.last_name=lname


        myuser.save()

        messages.success(request, 'User Registered successfully')

    return render(request,'authentication/signup.html')

# Create your views here.


def login_user(request):
    
    if request.method == "POST":   # view function called by submitting a form
        uname = request.POST['txtUname']
        upass = request.POST['txtPass']

        myuser = authenticate(username = uname, password = upass)

        if myuser is None:  # authentication failed
            messages.warning(request, 'Incorrect credential. Please try again')
            return redirect('login')
        else:   # successful
            login(request, myuser)   # login
            messages.success(request, 'Login successfull')
            if myuser.is_staff:
                #return render(request, 'authentication/dashboard.html')


                return redirect('home') # calls the view function responsible for rendering dashboard page after gathering required data 
            else:
                userprofile=UserProfile.objects.get(user__id=myuser.id) #get profile of logged in user
                savedcart=userprofile.oldcart #get stored cart items from db
                if savedcart:
                    savedcart=json.loads(savedcart) #loads function converts the string
                    mycart=Cart(request)
                    for k,v in savedcart.items():
                        mycart.updatecartfromdb(prodid=k,pqty=v)
                        
                return redirect('home')


    return render(request, 'authentication/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, 'Logout successful')
    return redirect('home')

# def dashboard_page(request):
#     if request.user.is_authenticated:
#         if request.user.is_staff:
#             allfb=Feedback.objects.all()
#             context={"feedbacks":allfb}

#         return render(request, 'authentication/dashboard.html', context)
#     else:
#         messages.warning(request, "You are not authorized to access this page. Please login")
#         return redirect('home')
    
# def changepass_user(request):

#     if request.method == "POST":
#         oldpass = request.POST['txtOPass']
#         newpass = request.POST['txtNPass']
#         confpass = request.POST['txtConfPass']
#         uname = request.user.username # grab username of logged in user from session

#         myuser = authenticate(username = uname, password = oldpass) # authenticate with current password
        
#         if myuser is not None:  # authenticated
            
#             myuser.set_password(newpass)
#             myuser.save()

#             messages.success(request, 'Password changed successfully')
#             return redirect('dashboard')

#     return render(request, 'authentication/change_pass.html')
