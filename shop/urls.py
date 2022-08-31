from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="ShopAbout"),
    path('contact/', views.contact, name="ShopContact"),
    path('track/', views.tracker, name="ShopTracker"),
    path('search/', views.search, name="ShopSerach"),
    path('products/', views.products, name="ShopProducts"),
    path('product/', views.product, name="ShopProduct"),
    path('checkout/', views.checkout, name="ShopCheckout"),
]