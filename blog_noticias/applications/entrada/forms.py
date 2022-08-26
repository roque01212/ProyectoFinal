from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    """Form definition for MODELNAME."""
    class Meta:
        """Meta definition for MODELNAMEform."""

        model = Entry
        fields = (
            'category',
            'title',
            'resume',
            'content',
            'image',
        )

        widgets={
            'resume':forms.Textarea(
                attrs={
                    'placeholder':'Correo Electronico...',
                    'cols':30,
                    'rows':10
                    
                }
            )
        }
