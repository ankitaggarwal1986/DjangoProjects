from distutils.command.upload import upload
from turtle import color
from unicodedata import name
from django.db import models
from numpy import size

# Create your models here.
class MainCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    maincat = models.ForeignKey(MainCategory, on_delete=models.CASCADE)
    subcat = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    baseprice = models.IntegerField()
    discount = models.IntegerField(default=0)
    finalprice = models.IntegerField()
    color= models.CharField(max_length=20)
    size = models.CharField(max_length=10)
    description = models.TextField()
    stock = models.BooleanField(default=True)
    time = models.DateTimeField(auto_now=True)
    pic1 = models.ImageField(upload_to="images/")
    pic2 = models.ImageField(upload_to="images/")
    pic3 = models.ImageField(upload_to="images/")
    pic4 = models.ImageField(upload_to="images/")

    def __str__(self):
        return str(self.id)+" "+self.name


    


