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
def shops_d_view (request , id ):
    if request.method =='GET':
        shop = Product.objects.get(id=id)
        context_data = {'shops': shop}
    return render(request, 'shops/detail.html', context=context_data)
def buy_d_view (request , id ):
    if request.method =='GET':
        shop = Product.objects.get(id=id)
        context_data = {'shops': shop}
    return render(request, 'shops/buy.html', context=context_data)