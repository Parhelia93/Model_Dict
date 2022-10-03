import re
from django.shortcuts import render, HttpResponse, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cat, Owner, Person, Word, WordDetail, WordStat, PersonWordList
from .serializers import CatSerializer, OwnerSerializer, PersonSerializer, WordSerializer, WordStatSerializer, PersonWordListSerializer, UpdatePersonWordSerializer, WordDetailSerializer, PersonWordSerializer
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import viewsets
import random
from .data_fetcher import get_random_word
from django.core.exceptions import ObjectDoesNotExist

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

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer 

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer 

class WordStatViewSet(viewsets.ModelViewSet):
    queryset = WordStat.objects.all()
    serializer_class = WordStatSerializer 

# class PersonWordListViewSet(viewsets.ModelViewSet):
#     queryset = PersonWordList.objects.all()
#     serializer_class = PersonWordListSerializer 

class PersonWordListViewSet(generics.ListAPIView):
    serializer_class = PersonWordListSerializer 

    def get_queryset(self):
        queryset = PersonWordList.objects.all()
        telegram_id = self.kwargs['telegram_id']
        if telegram_id is not None:
            person = Person.objects.get(telegram_id=telegram_id)
            queryset = queryset.filter(person=person)
        return queryset


class PersonWordApi(generics.RetrieveAPIView):
    serializer_class = WordDetailSerializer

    def get_queryset(self):
        telegram_id = self.request.query_params.get('telegram_id')
        try:
            person = Person.objects.get(telegram_id=telegram_id)
        except ObjectDoesNotExist:
            person = None
        person_word_list = PersonWordList.objects.filter(person=person)
        return get_random_word(person_word_list)

    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset
        return obj
        
        

class ResultPersonApi(generics.UpdateAPIView):
    serializer_class = WordStatSerializer
    queryset = WordStat.objects.all()
    
    def get_queryset(self):
        pk = self.request.data.get('pk')
        answer = self.request.data.get('answer')
        stat = WordStat.objects.get(pk=pk)
        if answer == 'True':
            stat.true_answer+=1
        else:
            stat.false_answer+=1

        if stat:
            return stat
        return None
        
    def get_object(self):
        queryset = self.get_queryset()
        obj = queryset
        return obj
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "updated successfully"})
        else:
            return Response({"message": "failed", "details": serializer.errors})
