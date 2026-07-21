from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('shop/', views.shop_view, name='shop'),
    path('blog/', views.blog_view, name='blog'),
    path('blog-details/', views.blog_details_view, name='blog-details'),
    path('contact/', views.contact_view, name='contact'),
    path('shopping-cart/', views.cart_view, name='shopping-cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('faq/', views.faq_view, name='faq'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]