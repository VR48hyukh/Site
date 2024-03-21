from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from rest_framework import generics
from rest_framework.response import Response

from rest_framework.views import APIView
from .models import Photo, Gallery
from .serializers import PhotoSerializer, GallerySerializer


class PhotoView(generics.ListCreateAPIView):
    queryset=Photo.objects.all()
    serializer_class=PhotoSerializer




class GalleryView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Gallery.objects.all()
    serializer_class = GallerySerializer