from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product, Category, Customer
from django.contrib.auth.hashers import make_password, check_password
# Create your views here.


def index(request):
        products = Product.objects.all()
        categories = Category.objects.all()
        email = request.session.get('customer_email')
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, 'index.html', context)


def about(request):
    return None


def collection(request):
    if request.method == "GET":
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products_collection = None
        categories_collection = Category.objects.all()
        categoryfilter = request.GET.get('category')
        if categoryfilter:
            products_collection = Product.objects.filter(categories=categoryfilter, )
        else:
            products_collection = Product.objects.all()

        context = {
            'products': products_collection,
            'categories': categories_collection
        }
        return render(request, 'collection.html', context)

    else:
        product = request.POST.get('product')
        cart = request.session.get('cart')
        remove = request.POST.get('remove')
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    else:
                        cart[product] = quantity-1
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1
        request.session['cart'] = cart

        return redirect('collection')


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        password = request.POST.get('password')
        password = make_password(password)

        email_exists = None
        if Customer.objects.filter(email=email, ):
            email_exists = True
        else:
            email_exists = False
        value = {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": phone_number,
        }

        error_message = None

        if not first_name:
            error_message = "First Name is Required!!!"
        elif not last_name:
            error_message = "Last Name is Required!!!"
        elif email_exists:
            error_message = "Email is Already Registered"
        elif not email:
            error_message = "E-Mail is Required!!!"
        elif not phone_number:
            error_message = "Phone Number is Required!!!"
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
            messages.success(request, "New User Registered Successfully")
            return redirect('signup')
        else:
            context = {
                "error_message": error_message,
                "values": value
            }
            return render(request, 'signup.html', context)

    else:
        return render(request, 'signup.html', {})


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.objects.get(email=email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer_id'] = customer.id
                request.session['customer_email'] = customer.email
                return redirect('index_shop')
            else:
                error_message = "Email/Password is Wrong !!! Plzz Try Again"

        else:
            error_message = "Email/Password is Wrong !!! Plzz Try Again"
        context = {
            "error_message": error_message
        }

        return render(request, 'login.html', context)
    else:
        return render(request, 'login.html', {})

