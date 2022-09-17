# from django.urls import path
# from .views import *

# urlpatterns = [
#     # path('cats/', cat_list, name='cat_list'),
#     path('hello/', CatListApi.as_view(), name='hello'),
#     path('hello/<int:pk>/', CatDetailApi.as_view(), name='hello1'),
# ]

from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import *


router = DefaultRouter()
router.register('cats', CatViewSet)
router.register('owners', OwnerViewSet)

urlpatterns = [
    path('', include(router.urls)),
] 