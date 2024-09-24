from django.db.models import Count
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from olcha.models import Category, Group
from olcha.serializers import CategorySerializer, GroupSerializer


class CategoryDetailApiView(APIView):
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        serializer = CategorySerializer(category, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CategoryListApiView(APIView):

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

