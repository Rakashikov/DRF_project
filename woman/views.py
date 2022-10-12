from django.shortcuts import render
from rest_framework import generics

from .models import Woman
from .serializers import WomanSerializer


class WomanApiView(generics.ListAPIView):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer
