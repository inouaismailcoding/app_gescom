from django import forms
from django.forms import ModelForm
from .models import *


class ArticleForm(forms.ModelForm):

    class Meta:
        model=Article
        fields=['category','article','img_article','package','price']


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['category','image']

class PackageForm(forms.ModelForm):
    class Meta:
        model=Package
        fields=['package']

    