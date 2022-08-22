

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms

class User_registrations_form(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label='password',widget=forms.PasswordInput)
    password2= forms.CharField(label='password confirmation',widget=forms.PasswordInput)
    image= forms.ImageField()
    phone= forms.CharField()
    address= forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ('username','email','password1','password2','image','phone','address')
        help_texts = {k:'' for k in fields}