from .models import ImageModel,UploadVideo
from django import forms
class ImageForm(forms.ModelForm):
    class Meta:
        model=ImageModel
        fields='__all__'

class UploadForm(forms.ModelForm):
    class Meta:
        model=ImageModel
        fields='__all__'