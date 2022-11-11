from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Woman
from .serializers import WomanSerializer


class WomanViewSet(viewsets.ModelViewSet):
    queryset = Woman.objects.all()
    serializer_class = WomanSerializer


# class WomanAPIListCreateView(generics.ListCreateAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
#
#
# class WomanAPIUpdateView(generics.UpdateAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
#
#
# class WomanAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
