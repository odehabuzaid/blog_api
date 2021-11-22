from blog import serializer
from rest_framework import generics

from .models import VPost


class VPostsList(generics.ListCreateAPIView):
    queryset = VPost.objects.all()
    serializer_class = serializer.VPostSerializer


class VPostsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VPost.objects.all()
    serializer_class = serializer.VPostSerializer
