from django.shortcuts import render, HttpResponse
from .models import Category, Company, Product

def index(request):
    #food is a list of objects
    food = Category.objects.all()
    companies = Company.objects.all()
    products = Product.objects.all()
    print(food)
    return render(request, "index.html", {
        "type": food, 
        "brands": companies,
        "item": products
        })


