from django import forms
from django.forms import ModelForm

from .models import Category
from .models import Product


class ProdForm(ModelForm):
    # nested class
    class Meta:  # connects the model to the form
        model = Product
        fields= "__all__"

        # fields = ('name', 'img')  # form built based on the specified fields

        labels = {
            'name': 'Enter product name',
            'desc' : 'Describe the product',
            'img' : 'Upload an image'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'menu name'}),  # form-control is  bootstrap class 
            'desc' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Details'}),
        }

class CategoryForm(ModelForm):
    # nested class
    class Meta:  # connects the model to the form
        model = Category
        fields= "__all__"

        # fields = ('name', 'img')  # form built based on the specified fields

        labels = {
            'name': 'Enter category name',
            'desc' : 'Describe the category',
            'img' : 'Upload an image'
        }

        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'category name'}),  # form-control is  bootstrap class 
            'desc' : forms.Textarea(attrs={'class': 'form-control', 'placeholder' : 'Details'}),
        }

        


       