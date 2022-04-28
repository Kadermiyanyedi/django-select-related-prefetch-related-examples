from rest_framework import routers

from product.api.views import ProductViewSet

router = routers.DefaultRouter()

router.register("products", ProductViewSet, basename="product")
