from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend

from posts.serializers import PostSerializer
from .permissions import IsAuthorOrReadOnlyPermission
from .models import * 
from .serializers import *
# Create your views here.


class PostViewSet(ModelViewSet):
    permission_classes = [IsAuthorOrReadOnlyPermission,]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category', 'tag']

class CategoryViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TagViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CommentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeOrDislikeViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = LikeDislike.objects.all()
    serializer_class = LikeDislikeSerializer