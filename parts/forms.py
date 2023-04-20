from django.forms import ModelForm
from .models import Part
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import  AuthenticationForm


class PartForm(ModelForm):
   class Meta:
        model = Part
        fields = ['title','part_no','slug','danish_slug','out_of_stock','inactive', 'bike_models']
        widgets = {
            'title': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'name'}),
            'part_no': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'SKU'}),
            #'expected_date': forms.widgets.DateInput(attrs={'type': 'date', "class": "form-control"}),
            'slug': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'slug'}),
            'danish_slug': forms.widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'dansk'}),
            'bike_models': forms.widgets.TextInput(attrs={'required': 'false','class': 'd-none'})
     }



class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    class Meta:
        model = User
        fields = ['username',]

class NewUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(max_length=100, required=True, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    class Meta:
        model = User
        fields = ['username','password',]
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(max_length=100, required=True, 
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'password'}))
    class Meta:
        model = User
        fields = ['username','password',]
