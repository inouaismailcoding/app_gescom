from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    class Meta:
            model =Customer
            fields =['customer','nui','rc','phone','mail','country','town']

class SaleLineForm(forms.ModelForm):   
    class Meta:
        model =SaleLine
        fields =['article','quantity','price','amount']

class SaleForm(forms.ModelForm):   
    class Meta:
        model =Sale
        fields =['customer','amount']