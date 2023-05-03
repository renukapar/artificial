from django.db import models

# Create your models here.
class ProductModel(models.Model):
    Productid=models.CharField(max_length=5,primary_key=True)
    Product_Name=models.CharField(max_length=10)
    Price=models.IntegerField()
    Review=models.CharField(max_length=5)

