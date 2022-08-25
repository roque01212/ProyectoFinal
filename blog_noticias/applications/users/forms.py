
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User_profile


from django import forms

class User_registrations_form(UserCreationForm):
    email= forms.EmailField(required=True)
    password1= forms.CharField(label='password',widget=forms.PasswordInput)
    password2= forms.CharField(label='password confirmation',widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        help_texts = {k:'' for k in fields}
    


class UserForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for Userform."""

        model = User_profile
        fields = (
            'phone',
            'address',
            'email',
            'image',
        )
