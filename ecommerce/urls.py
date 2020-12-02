from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_shop'),
    path('about/', views.about, name='about'),
    path('collection/', views.collection, name='collection'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),

]

