from django import forms
from .models import *


class IntervenantForm(forms.ModelForm):
    class Meta:
        model =Intervenant
        fields =['intervenant','matricule','post_occuped','direction','dept','phone','mail','town']

class TransactionLineForm(forms.ModelForm):
    class Meta:
        model:TransactionLine
        fields=['article','quantity']

class TransactionForm(forms.ModelForm):
    class Meta:
        model:Transaction
        fields=['intervenant','mouvement','full_quantity']


class TransactionDataForm(forms.ModelForm):   
    class Meta:
        model =Transaction
        fields =['intervenant','mouvement','full_quantity']

class TransactionDataLineForm(forms.ModelForm):   
    class Meta:
        model =TransactionLine
        fields=['article','quantity']

