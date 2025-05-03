from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def cart(request):
    return render(request, 'core/cart.html')

def checkout(request):
    return render(request, 'core/checkout.html')

def contact(request):
    return render(request, 'core/contact.html')

def shop_single(request):
    return render(request, 'core/shop-single.html')

def shop(request):
    return render(request, 'core/shop.html')

def thankyou(request):
    return render(request, 'core/thankyou.html')

def base(request):
    return render(request, 'core/base.html')
