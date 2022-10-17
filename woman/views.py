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
        post_new = Woman.objects.create(
            title=req.data['title'],
            content=req.data['content'],
            category_id=req.data['category_id']
        )
        return Response({'post': WomanSerializer(post_new).data})


# class WomanApiView(generics.ListAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
