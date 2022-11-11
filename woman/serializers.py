import io

from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Woman


class WomanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Woman
        fields = ('id', 'title', 'content', 'time_create', 'time_update', 'is_published', 'category')
