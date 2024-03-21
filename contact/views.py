from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views.generic import CreateView
from rest_framework import generics
from rest_framework.response import Response

from rest_framework.views import APIView

from .models import ContactLink, About, ContactModel
from .forms import ContactForm
from .serializers import ContactLinkSerializer, AboutSerializer, ContactModelSerializer


class ContactListView(generics.ListAPIView):
    queryset=ContactLink.objects.all()
    serializer_class = ContactLinkSerializer
    def get(self, request):
        contacts = ContactLink.objects.all()
        form = ContactForm()
        return render(request, 'templates/home.html', {"home": contacts, "form": form})




class AboutView(APIView):
    serializer_class = AboutSerializer
    def get(self, request, pk):
        w=About.objects.all()
        return Response({"post":AboutSerializer(w, many=True).data})

    def post(self, request):
        serializer=AboutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def put(self, request,*args, **kwargs):
        pk= kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method PUT not allowed"})

        try:
            instance = About.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = AboutSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"post": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method DELETE not allowed"})

        # здесь код для удаления записи с переданным pk

        return Response({"post": "delete post " + str(pk)})
class ContactModelList(generics.ListAPIView):
    queryset = ContactModel.objects.all()
    serializer_class = ContactModelSerializer

