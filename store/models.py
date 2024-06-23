from django.db import models
from .utilities import get_file_path
from django.contrib.auth.models  import User
from django.db.models.signals import post_save

# Create your models here.

class Category (models.Model):
    name= models.CharField(max_length=50)
    cat_id=models.AutoField(primary_key=True)
  
    # img = models.ImageField(null = True, blank = True, upload_to='images/')
    #img = models.ImageField(null = True, blank = True, upload_to=get_file_path)
    
    
    def __str__(self) :
        return self.name
    
class Product(models.Model):
    p_id= models.AutoField(primary_key = True)
    p_name= models.CharField(max_length=50)
    p_desc= models.TextField()
    p_price = models.DecimalField(max_digits = 9, decimal_places = 2)
    p_cat = models.ForeignKey(Category, on_delete=models.CASCADE, default = 1)  # maps the fkey to the Primary Key of the Cuisine table
    img = models.ImageField(null = True, blank = True, upload_to=get_file_path)
    on_sale=models.BooleanField(default=False)
    saleprice=models.DecimalField(max_digits = 9, decimal_places = 2,default=0)

    def __str__(self) :
        return self.p_name
    

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    date_mod=models.DateTimeField(User,auto_now=True)
    phoneno=models.CharField(max_length=10)
    addr=models.TextField(max_length=100)
    city=models.TextField(max_length=50)
    pin=models.CharField(max_length=15)
    oldcart=models.CharField(max_length=300,blank=True)
    def __str__(self) :
        return self.user.username
 
def create_profile(sender,instance,created, **kwargs):
        if created:
            user_profile=UserProfile(user=instance)
            user_profile.save()


post_save.connect(create_profile,sender=User)


    
  


    

    
   