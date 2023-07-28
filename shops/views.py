from django.shortcuts import render, HttpResponse,redirect
import datetime
# Create your views here.
from shops.models import Product, Category ,Comment
from shops.forms import Category_create,Product_create ,CommentsCreateForm


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
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': CommentsCreateForm
        }

        return render(request, 'shops/detail.html', context=context)

    if request.method == 'POST':
        product = Product.objects.get(id=id)
        data = request.POST
        form = CommentsCreateForm(data=data)

        if form.is_valid():
            Comment.objects.create(
                text=form.cleaned_data.get('text'),
                product=product

            )

        context = {
            'product': product,
            'comments': product.comment_set.all(),
            'form': form
        }

        return render(request, 'shops/detail.html', context=context)
def create_product_view(request):
    if request.method == 'GET':
        context_data = {'form': Product_create}
        return render(request, 'shops/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = Product_create(data, files)
        if form.is_valid():
            Product.objects.create(
                img=form.cleaned_data.get('img'),
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                rate=form.cleaned_data.get('rate'),
                category=form.cleaned_data.get('category'),
                prize=form.cleaned_data.get('prize'),
                phone_number=form.cleaned_data.get('phone_number')

            )
            return redirect('/shops/')
        return render(request, 'shops/create.html', context={'form': form})


def create_category_view(request):
    if request.method == 'GET':
        context_data = {'form': Category_create}

        return render(request, 'shops/catergory/category_create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        f = Category_create(data, files)

        if f.is_valid():
            Category.objects.create(
                title=f.cleaned_data.get('title')

            )
            return redirect('/category/')
        return render(request, 'shops/catergory/category_create.html', context={'form': f})
