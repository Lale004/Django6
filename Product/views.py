from django.shortcuts import render
from .models import Product
def list1(request):
    products=Product.objects.all()
    context={'products': products}
    return render(request,'list1.html',context)

def list2(request):
    products=Product.objects.all()
    context={'products': products}
    return render(request,'list2.html',context )


# Create your views here.
