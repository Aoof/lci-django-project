from django.http.response import HttpResponse
from django.shortcuts import render
from product.models import Product


def accueil(request):
    all_products = Product.objects.all()
    return render(request, "index.html", {"products": all_products})


def contact(request):
    return render(request, "contact.html")
