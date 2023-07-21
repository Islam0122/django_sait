from django.shortcuts import render, HttpResponse
import datetime
# Create your views here.
from shops.models import Product, Category


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def shops_view(request):
    if request.method == 'GET':
        Shops = Product.objects.all()
        context_data = {'shops': Shops}
        return render(request, 'shops/shops.html', context=context_data)


def category_view(request):
    if request.method == 'GET':
        category = Category.objects.all()
        context_data = {'category': category}
        return render(request, 'shops/catergory/catergories.html', context=context_data)
