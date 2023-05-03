from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class CustomerModel(models.Model):
    First_Name=models.CharField(max_length=10)
    Last_Name=models.CharField(max_length=10)
    Company=models.CharField(max_length=10)
    Email=models.EmailField()
    Phone_no=models.IntegerField()
    plan = [('Business','Business'), ('Enterprise', 'Enterprise'), ('Other', 'Other')]
    Plans= models.CharField(max_length=10, choices=plan, default='Enterprise')
    Msg=models.TextField()