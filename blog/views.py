from django.shortcuts import render
from django.views import View

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Comment, Recipe
from .forms import CommentForm
from .serializers import HomeSerializer, CommentSerialzer, RecipeSerializer, PostSerializer



class HomeView(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=HomeSerializer

class CommentView(generics.ListAPIView):
    queryset=Comment.objects.all()
    serializer_class=CommentSerialzer


class PostListView(APIView):
    def get(self, request):
        queryset=Post.objects.all()
        return Response({'post':PostSerializer(queryset, many=True).data})
    def post(self, request):
        serializer=PostSerializer
        serializer.is_valid(raise_exception=True)



class RecipeListView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerialzer
    form_class = CommentForm

    def form_valid(self, form):
        form.instance.post_id = self.kwargs.get('pk')
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self, request):
        return self.object.post.get_absolute_url()