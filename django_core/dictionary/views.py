from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Person
from .serializers import AlbumSerializer
# Create your views here.

class AlbumAPIView(APIView):
    def get(self, request):
        w = Person.objects.all()
        return Response({'post':AlbumSerializer(w, many=True).data})
