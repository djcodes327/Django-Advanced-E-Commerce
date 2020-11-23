from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category

# Create your views here.


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'index.html', context)


def about(request):
    return None


def collection(request):
    products_collection = None
    categories_collection = Category.objects.all()
    categoryfilter = request.GET.get('category')
    print(request.GET.get('category'))
    if categoryfilter:
        products_collection = Product.objects.filter(categories=categoryfilter,)
    else:
        products_collection = Product.objects.all()

    context = {
        'products': products_collection,
        'categories': categories_collection
    }
    return render(request, 'collection.html', context)