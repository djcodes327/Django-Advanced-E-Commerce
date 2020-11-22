from math import ceil
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n // 4 + ceil((n / 4) + (n // 4))
    context = {
        'no_of_slides': nSlides,
        'range': range(1, nSlides),
        'product': products
    }
    return render(request, 'index.html', context)


def about(request):
    return None