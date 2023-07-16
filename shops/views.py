from django.shortcuts import render , HttpResponse
import datetime
# Create your views here.
from shops.models import  Product
def main_view(request):
    if request.method == 'GET':
        return render(request,'layouts/index.html')
def shops_view(request):
    if request.method == 'GET':
        Shops = Product.objects.all()
        context_data = {'shops': Shops}
        return render(request,'shops/shops.html',context=context_data)

