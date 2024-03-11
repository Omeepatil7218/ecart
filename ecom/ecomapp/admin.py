from django.contrib import admin
from ecomapp.models import Product

# Register your models here.
# admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields=['id','name','price','ptdetails','is_active','image']
    
# admin.site.register(ProductAdmin,Product)