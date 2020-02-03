from django.shortcuts import render
from user.models import Post
from .serializer import PostSerializer
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('id')
    serializer_class = PostSerializer



