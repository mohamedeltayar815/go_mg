from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class CustomerForm(ModelForm):
	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ['user']

class OrderForm(ModelForm):
	class Meta:
		model = Order
		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


class massageForm(ModelForm):
	class Meta:
		model = massage
		fields = '__all__'





class commentForm(ModelForm):
	class Meta:
		model = coment
		fields = '__all__'



class comment1Form(ModelForm):
	class Meta:
		model = coment1
		fields = '__all__'

