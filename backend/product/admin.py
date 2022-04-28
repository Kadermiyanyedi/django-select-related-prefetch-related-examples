from attr import fields
from django.contrib import admin

from product.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "seller")
    list_filter = ("country__name",)
    autocomplete_fields = ("country", "seller")
    fields = ("name", "seller", "country", "is_active")
