from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "product_name",
        "price",
        "stock",
        "is_available",
        "category",
        "modified_date",
    )
    prepopulated_fields = {"slug": ("product_name",)}
    # list_editable = ("price", "stock", "is_available")
    # search_fields = ("product_name", "category__category_name")
    # list_filter = ("is_available", "category")


admin.site.register(Product, ProductAdmin)
