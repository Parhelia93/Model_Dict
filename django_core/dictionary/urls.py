from django.urls import path
from .views import *

urlpatterns = [
    path('cats/', cat_list, name='cat_list'),
    path('hello/', hello, name='hello'),
    path('hello/<int:pk>/', hello1, name='hello1'),
]