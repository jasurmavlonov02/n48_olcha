from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from olcha.models import Product, Image
from olcha.serializers import ProductSerializer, ImageSerializer


class ProductListApiView(ListCreateAPIView):
    permission_classes = [AllowAny]
    # authentication_classes = [JWTAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ImageListApiView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# Hello Guys