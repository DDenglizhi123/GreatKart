<<<<<<< HEAD
from django.shortcuts import get_object_or_404, render
from category.models import Category
from store.models import Product
=======
from django.shortcuts import render, get_object_or_404

from category.models import Category
from .models import Product
>>>>>>> d4184a5 (updates)


# Create your views here.
def store(request, category_slug=None):
<<<<<<< HEAD
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()

    context = {
        "products": products,
        "product_count": product_count,
    }
    return render(
        request,
        "store/store.html",
        context,
    )
=======
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True)
        products_count = products.count()
    context = {"products": products, "products_count": products_count}
    return render(request, "store/store.html", context)
>>>>>>> d4184a5 (updates)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug
        )
    except Exception as e:
        raise e
<<<<<<< HEAD

    context = {
        "single_product": single_product,
    }
=======
    context = {"single_product": single_product}
>>>>>>> d4184a5 (updates)
    return render(request, "store/product_detail.html", context)
