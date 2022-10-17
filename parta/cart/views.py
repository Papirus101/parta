from rest_framework import generics
from rest_framework.views import Response
from .models import Products, Tariff
from .serializers import PrductsPriceSerializer, ProductsSerializer

class ProductsApiView(generics.ListAPIView):
    """
    Query Parameters
    `class_product` - filter products by class
    """
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()

    def get_queryset(self):
        serializer = self.serializer_class()
        serializer_data = serializer.get_products(class_product=self.request.query_params.get('class_product'))
        return serializer_data.data


class ProductsPriceApiView(generics.GenericAPIView):
    """
    Request Parameters
    { "product ID": tariff ID }
    """
    serializer_class = PrductsPriceSerializer
    queryset = []

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save(request=dict(request.data))
        return Response(data)

