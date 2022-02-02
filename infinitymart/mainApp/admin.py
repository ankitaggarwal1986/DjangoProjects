from django.contrib import admin
from .models import MainCategory,SubCategory,Brand,Product

# Register your models here.
admin.site.register((MainCategory,
                    SubCategory,
                    Brand,
                    Product))