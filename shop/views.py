from django.shortcuts import render

# Create your views here.


def indexs(request):
    return render(request,'index.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def faq(request):
    return render(request,faq.html)

def product_detais(request):
    return render(request,'product-detail.html')

def products(request):
    return render(request,'products.html')

def signup(request):
    return render(request,'sign-up.html')
def signin(request):
    return render (request,'sign-in.html')