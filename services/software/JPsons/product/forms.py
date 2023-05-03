from .models import ProductModel
from django import forms
class ProductForm(forms.ModelForm):
    class Meta:
        model=ProductModel
        fields='__all__'


