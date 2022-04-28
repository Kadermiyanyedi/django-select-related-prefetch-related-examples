from rest_framework import mixins, viewsets

from product.api.serializers import ProductSerializer
from product.models import Product


class ProductViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
