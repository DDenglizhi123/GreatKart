from django.urls import path
<<<<<<< HEAD
from .views import *

urlpatterns = [
    path("", store, name="store"),
    path("<slug:category_slug>/", store, name="products_by_category"),
    path(
        "<slug:category_slug>/<slug:product_slug>/",
        product_detail,
=======
from . import views

urlpatterns = [
    path("", views.store, name="store"),
    path("<slug:category_slug>/", views.store, name="products_by_category"),
    path(
        "<slug:category_slug>/<slug:product_slug>/",
        views.product_detail,
>>>>>>> d4184a5 (updates)
        name="product_detail",
    ),
]
