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
router.register('persons', PersonViewSet)
router.register('words', WordViewSet)
router.register('wordsstat', WordStatViewSet)
# router.register('personwordlist', PersonWordListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('personwordlist/<str:telegram_id>/', PersonWordListViewSet.as_view()),
    path('updatepersonword/<str:telegram_id>/', UpdatePersonWordList.as_view())
] 