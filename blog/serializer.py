from rest_framework import serializers
from vlogs import models

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "body", "author")


class VPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VPost
        fields = ("id", "title", "v_url", "body", "author")
