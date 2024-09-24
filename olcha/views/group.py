from django.db.models import Count
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from olcha.models import Category, Group
from olcha.serializers import CategorySerializer, GroupSerializer


class GroupListApiView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

