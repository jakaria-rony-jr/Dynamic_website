from django import forms
from .models import ContactForm

class Contact_f(forms.ModelForm):
    class Meta:
        model = ContactForm 
        fields = "__all__"
