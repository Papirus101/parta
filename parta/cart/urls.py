from django.urls import include, path
from rest_framework import routers
from .base_router import HybridRouter
from .views import ProductsApiView, ProductsPriceApiView

router = HybridRouter()
router.add_api_view('products', path('products/', ProductsApiView.as_view(), name='products'))
router.add_api_view('products_price', path('products_price', ProductsPriceApiView.as_view(), name='products_price'))

urlpatterns = [
    path("", include(router.urls)),
]
