import imp
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    data=Product.objects.all()
    data=data[::-1]
    return render(request, "index.html", {"Data":data})
