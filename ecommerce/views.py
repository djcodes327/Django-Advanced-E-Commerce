from math import ceil
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Category, Customer
from .forms import UserForm

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
        products_collection = Product.objects.filter(categories=categoryfilter, )
    else:
        products_collection = Product.objects.all()

    context = {
        'products': products_collection,
        'categories': categories_collection
    }
    return render(request, 'collection.html', context)


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')

        error_message = None
        if not first_name:
            error_message = "First Name is Required!!!"
        elif not last_name:
            error_message = "Last Name is Required!!!"
        elif not phone_number:
            error_message = "Phone Number is Required!!!"
        elif not email:
            error_message = "E-Mail is Required!!!"
        elif len(phone_number) <= 9:
            error_message = "Please Enter a Valid Phone Number"
        elif not password:
            error_message = "Password is Required!!!"

        if not error_message:
            Customer.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone_number=phone_number,
                password=password,
            )
            messages.success(request, "New User Added Successfully")
            return redirect('signup')
        else:
            context = {
                "error_message": error_message
            }
            return render(request, 'signup.html', context)


    else:
        return render(request, 'signup.html', {})
