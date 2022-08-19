from django import forms

from .models import Suscribers

class SuscribersForm(forms.ModelForm):
    """Form definition for Suscribers."""

    class Meta:
        
        model = Suscribers
        fields = ('email',)

