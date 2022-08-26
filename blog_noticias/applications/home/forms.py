from django import forms
from .models import Suscribers
from .models import Suscribers, Contact


class SuscribersForm(forms.ModelForm):
    """Form definition for Suscribers."""

    class Meta:
        
        model = Suscribers
        fields = ('email',)



class ContactForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = ('__all__')

