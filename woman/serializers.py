import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Woman


class WomanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woman
        fields = ('id', 'title', 'content', 'time_create', 'time_update', 'is_published', 'category')

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
