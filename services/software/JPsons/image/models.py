from django.db import models

# Create your models here.

class ImageModel(models.Model):
    Product=models.CharField(max_length=10)
    Image=models.ImageField(upload_to='static/img/')

class UploadVideo(models.Model):
    details = models.CharField(max_length=20)
    video = models.FileField(upload_to='videos/')