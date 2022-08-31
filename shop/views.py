from django.shortcuts import HttpResponse, render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def tracker(request):
    return render(request, '')

def search(request):
    return render(request, '')

def products(request):
    return render(request, 'products.html')

def product(request):
    return render(request, 'product.html')

def checkout(request):
    return render(request, 'checkout.html')
