from django.urls import path
from .import views

urlpatterns = [
    path('home/',views.indexs,name='home'),
    path('about/',views.about,name='about'),
    path('contract/',views.contact,name='contract'),
    path('faq/',views.faq,name='faq'),
    path('productdetais/',views.product_detais,name='productdetais'),
    path('products/',views.products,name='products'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
]
