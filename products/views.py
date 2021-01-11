from django.shortcuts import render
from .models import products

# Create your views here.

def all_products(request):
    """ A view to return the prodcust page and to handle search query results on products searches """

    products = Products.objects.all()

    context = {
        'products' : products
    }

    return render(request, 'products/products.html' colntext)
