from django.shortcuts import render

# Core pages you created
def home_view(request):
    return render(request, 'index.html')

def shop_view(request):
    return render(request, 'product.html')

def contact_view(request):
    return render(request, 'contact.html')

# Remaining placeholder views to keep the server from crashing
def blog_view(request):
    return render(request, 'blog.html')

def blog_details_view(request):
    return render(request, 'blog-details.html')

def cart_view(request):
    return render(request, 'shopping-cart.html')

def checkout_view(request):
    return render(request, 'check-out.html')

def faq_view(request):
    return render(request, 'faq.html')

def register_view(request):
    return render(request, 'register.html')

def login_view(request):
    return render(request, 'login.html')