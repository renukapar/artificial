from.models import CustomerModel
from django.contrib.auth.models import User
from django import forms
class CustomerForm(forms.ModelForm):
    class Meta:
        model=CustomerModel
        fields='__all__'

class SignForm(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'