from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Woman
from .serializers import WomanSerializer


class WomanApiView(APIView):
    def get(self, req):
        w = Woman.objects.all()
        return Response({'posts': WomanSerializer(w, many=True).data})

    def post(self, req):
        serializer = WomanSerializer(data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def put(self, req, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})

        try:
            instance = Woman.objects.get(pk=pk)
        except:
            return Response({'error': 'Object not found'})

        serializer = WomanSerializer(instance, data=req.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post': serializer.data})

    def delete(self, req, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})

        try:
            instance = Woman.objects.get(pk=pk)
        except:
            return Response({'error': 'Object not found'})

        instance.delete()
        return Response({'post': 'deleted post #{}'.format(pk)})

# class WomanApiView(generics.ListAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
