from .import views
from django.urls import path




urlpatterns = [
   
    path('register/', views.signup_page, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # path('dash/', views.dashboard_page, name='dashboard'),
    #path('changepass/', views.changepass_user, name='change-pass'),
     ]