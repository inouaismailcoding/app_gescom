from django import forms
from .models import *


class SupplierForm(forms.ModelForm):
    class Meta:
        model =Supplier
        fields =['supplier','nui','rc','phone','mail','country','town']


class PurchaseLineForm(forms.ModelForm):   
    class Meta:
        model =PurchaseLine
        fields =['article','quantity','price','amount']

class PurchaseForm(forms.ModelForm):   
    class Meta:
        model =Purchase
        fields =['supplier','amount']