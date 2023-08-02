from django.db.models import Q
from django.shortcuts import render, HttpResponse, redirect
import datetime
# Create your views here.
from shops.constants import PAGINATION_LIMIT
from shops.models import Product, Category, Comment
from shops.forms import Category_create, Product_create, CommentsCreateForm


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def shops_view(request):
    if request.method == 'GET':

        shops = Product.objects.all()
        search_text = request.GET.get("search")
        page = int(request.GET.get('page', 1))
        if search_text:
            shops = shops.filter(Q(title__icontains=search_text) |
                                 Q(description__icontains=search_text)
                                 )

        max_page = shops.__len__() / PAGINATION_LIMIT
        max_page = round(max_page) + 1 if round(max_page) < max_page else round(max_page)

        shops = shops[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context_data = {
            'shops': shops,
            "user": request.user,
            'pages': range(1, max_page + 1)
        }
    return render(request, 'shops/shops.html', context=context_data)


def category_view(request):
    if request.method == 'GET':
        category = Category.objects.all()

        search_text = request.GET.get("search")

        if search_text:
            category = category.filter(title__icontains=search_text)

        context_data = {'category': category}
        return render(request, 'shops/catergory/catergories.html', context=context_data)


def shops_d_view(request, id):
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
                name=form.cleaned_data.get('name'),
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
