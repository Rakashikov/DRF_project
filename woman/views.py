from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView


from .models import Woman, Category
from .serializers import WomanSerializer


class WomanViewSet(viewsets.ModelViewSet):
    # queryset = Woman.objects.all()
    serializer_class = WomanSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Woman.objects.all()[:3]

        return Woman.objects.filter(pk=pk)

    @action(detail=True, methods=['get'])
    def category(self, request, pk=None):
        category = Category.objects.get(pk=pk)
        return Response({'category': category.name})


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
