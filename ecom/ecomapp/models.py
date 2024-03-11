from django.db import models
from django.contrib.auth.models import User
# Create your mdels here.
class Product(models.Model):
    CAT=(('mobile',1),('shoes',2),('clothes',3))
    name=models.CharField(max_length =50, verbose_name='product Name')
    price=models.FloatField()
    pdetails=models.CharField(max_length=50,verbose_name ='product details')
    cat=models.CharField( max_length=50,verbose_name="category",choices = CAT)
    is_active = models.BooleanField(default= True)
    image =models.ImageField(upload_to ='image')

# def __str__(self):
#     return self.name