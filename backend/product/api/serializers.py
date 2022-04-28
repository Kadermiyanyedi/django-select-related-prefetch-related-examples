from rest_framework import serializers

from address.api.serializers import CountryNestedSerializer
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    seller = serializers.CharField(source="seller.username", read_only=True)
    country = CountryNestedSerializer(many=True)

    class Meta:
        model = Product
        fields = ("id", "code", "name", "seller", "country")
