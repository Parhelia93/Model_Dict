from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cat, Owner
from .serializers import CatSerializer, OwnerSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets



# @api_view(['GET', 'POST'])
# def cat_list(request):
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     cats = Cat.objects.all()
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data) 



# @api_view(['GET', 'POST'])
# def hello(request):
#     if request.method == 'POST':
#         #return Response({'message': 'Получены данные', 'data': request.data})
#         serializer = CatSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(data=serializer.data)

# @api_view(['PATCH', 'DELETE'])
# def hello1(request, pk):
#     cat = Cat.objects.get(id=pk)
#     serializer = CatSerializer(instance=cat, data=request.data, partial=True)
#     if serializer.is_valid():
#         if request.method == 'PATCH':
#             serializer.save()
#         else:
#             cat.delete()
#         return Response(data=serializer.data)
#     return Response(data=serializer.errors)



# class CatListApi(APIView):
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(data=serializer.data)

#     def post(self, request):
#         serializer = CatSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# class CatDetailApi(APIView):
    
#     def patch(self, request, pk):
#         cat = Cat.objects.get(id=pk)
#         serializer = CatSerializer(instance=cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(data=serializer.data)
#         return Response(data=serializer.errors)

#     def delete(self, request, pk):
#         cat = Cat.objects.get(id=pk)
#         serializer = CatSerializer(instance=cat, data=request.data, partial=True)
#         if serializer.is_valid():
#             cat.delete()
#             return Response(data=serializer.data)
#         return Response(data=serializer.errors)

#     def get(self, request, pk):
#         try:
#             cat = Cat.objects.get(id=pk)
#         except:
#             return Response(status.HTTP_404_NOT_FOUND)
#         serializer = CatSerializer(cat)
#         return Response(data=serializer.data)
        


# class CatListApi(generics.ListCreateAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


# class CatDetailApi(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Cat.objects.all()
#     serializer_class = CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer 

