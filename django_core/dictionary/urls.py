from django.urls import path
from .views import *

urlpatterns = [
    path('cats/', cat_list, name='cat_list'),
    path('hello/', CatListApi.as_view(), name='hello'),
    path('hello/<int:pk>/', CatDetailApi.as_view(), name='hello1'),
]