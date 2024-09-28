from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from olcha.models import Product, Image
from olcha.serializers import ProductSerializer, ImageSerializer


class ProductListApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ImageListApiView(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
