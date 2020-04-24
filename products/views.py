from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .forms import ProductForm, ProductFormRaw
# Create your views here.

from .models import Product

def products(req,*args, **kwargs):
    products = Product.objects.all()
    # ? dir(here_is_the_object), is usefull when you are trying to see what methods or attributes are available in an object
    return render(req,"product/index.html",{"products":products})

def product(req,id,*args, **kwargs):
    print(id)
    product =get_object_or_404(Product,id=id)

    print(req.GET)
    data ={
        "title":product.title,
        "price":product.price,
        "description":product.description,
    }
    # ? dir(here_is_the_object), is usefull when you are trying to see what methods or attributes are available in an object
    return render(req,"product/product.html",data)


def create_product(req,*args, **kwargs):
    form = ProductForm(req.POST or None)
    # if al the values are valid then saves the information in the database
    if form.is_valid():
        form.save()
    
    return render(req,"product/create.html",{"form":form})

def create_product_raw_form(req,*args, **kwargs):
    name = req.POST.get("name")
    print(name,req.POST)
    
    return render(req,"product/rawForm.html",{})

def create_product_raw_form_class(req,*args, **kwargs):
    # if you want to put a default values to the form fields you can use instance and pass an instance of a db filter o a manual dict with the corresponding keys and values this is made with the param initial={<here_your_values>}
    
    my_form = ProductFormRaw(req.POST)
    if my_form.is_valid():
        print(my_form.cleaned_data)
        # with the ** you convert the data to a dict
        Product.objects.create(**my_form.cleaned_data)
    else:
        print(my_form.errors)
    return render(req,"product/rawForm.html",{"form":my_form})