from django.shortcuts import render
from .models import Product

def index(request):
    product = Product.objects.all()

    return render(request, template_name='app/product_list.html', context={'products': product})


