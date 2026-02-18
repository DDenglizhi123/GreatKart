from django.shortcuts import render
from store.models import Product


def home(request):
    products = Product.objects.all().filter(is_available=True)
<<<<<<< HEAD
    return render(request, "home.html", {"products": products})
=======
    context = {"products": products}
    return render(request, "home.html", context)
>>>>>>> d4184a5 (updates)
