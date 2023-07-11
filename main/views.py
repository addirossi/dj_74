from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from main.models import Product


def index_page(request):
    message = 'Привет всем, коллеги!'
    return HttpResponse(message)


def products_list(request):
    products = Product.objects.all()
    template_name = 'main/list.html'
    print(products[0].price)
    return render(request, template_name, {'products': products})


def product_details(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    template_name = 'main/details.html'
    return render(request, template_name, {'item': product})
