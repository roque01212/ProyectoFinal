from django import forms

<<<<<<< HEAD
from .models import Suscribers
=======
from .models import Suscribers, Contact
>>>>>>> roque

class SuscribersForm(forms.ModelForm):
    """Form definition for Suscribers."""

    class Meta:
        
        model = Suscribers
        fields = ('email',)

<<<<<<< HEAD
=======

class ContactForm(forms.ModelForm):
    """Form definition for Contact."""

    class Meta:
        """Meta definition for Contactform."""

        model = Contact
        fields = ('__all__')
>>>>>>> roque
