import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Woman


# class WomanModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomanSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    category_id = serializers.IntegerField()


# def encode():
#     model = WomanModel('title', 'content')
#     model_sr = WomanSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json, type(json), sep='\n')
#
# def decode():
#     stream = io.BytesIO(b'{"title": "title", "content": "content"}')
#     data = JSONRenderer().parse(stream)
#     serializer = WomanSerializer(data=data)
#     if serializer.is_valid():
#         print(serializer.validated_data)