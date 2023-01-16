from django.shortcuts import render
from rest_framework import generics

from .permissions import IsAdminAuthPermission
from .models import Post, Category, Tag
from .serializers import CategorySerializer, TagSerializer, PostSerializer, PostListSerializer
import django_filters
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


# class PostListCreateView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter]
#     filterset_fields = ['title', 'category', 'tags']
#     search_fields = ['tags__slug', 'created_at']


# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category']
    search_fields = ['tags__slug', 'created_at']
    ordering_fields = ['created_at', 'title']


    def get_serializer_class(self):
        if self.action == 'list':
            return PostListSerializer
        return self.serializer_class



    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [AllowAny]

        elif self.action == 'create':
            self.permission_classes = [IsAdminAuthPermission]

        elif self.action == ['update', 'partial_update', 'destroy']:
            self.permission_classes = ['только автор']
        


        # to_representation like, commenty
        # добавить 








