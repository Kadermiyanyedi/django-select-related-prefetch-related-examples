from django.db import connection, reset_queries
from django.db.models import Prefetch

from address.models import Country
from product.models import Product


def database_debug(func):
    def inner_func(*args, **kwargs):
        reset_queries()
        results = func()
        query_info = connection.queries
        print("function_name: {}".format(func.__name__))
        print("query_count: {}".format(len(query_info)))
        queries = ["{}\n".format(query["sql"]) for query in query_info]
        print("queries: \n{}".format("\n".join(queries)))
        return results

    return inner_func


@database_debug
def product_seller_name():
    products = Product.objects.all()
    return [product.seller.username for product in products]


@database_debug
def product_seller_name_with_select_related():
    products = Product.objects.all().select_related("seller")
    return [product.seller.username for product in products]


@database_debug
def country_products():
    countries = Country.objects.all()
    for country in countries:
        print(country.product_set.all())
    print()


@database_debug
def country_products_with_prefetch_related():
    countries = Country.objects.all().prefetch_related("product_set")
    for country in countries:
        print(country.product_set.all())
    print()


@database_debug
def get_country_product_seller():
    country = Country.objects.prefetch_related("product_set").get(pk=1)
    products = country.product_set.all()
    for product in products:
        print(product.seller)


@database_debug
def get_country_product_seller_high_performance():
    country = Country.objects.prefetch_related(
        Prefetch("product_set", queryset=Product.objects.select_related("seller"))
    ).get(pk=1)
    products = country.product_set.all()
    for product in products:
        print(product.seller)
