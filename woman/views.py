from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Woman
from .serializers import WomanSerializer


class WomanApiView(APIView):
    def get(self, req):
        lst = Woman.objects.all()
        return Response({'posts': list(lst.values())})

    def post(self, req):
        post_new = Woman.objects.create(
            title=req.data['title'],
            content=req.data['content'],
            category_id=req.data['category_id']
        )
        return Response({'post': model_to_dict(post_new)})


# class WomanApiView(generics.ListAPIView):
#     queryset = Woman.objects.all()
#     serializer_class = WomanSerializer
