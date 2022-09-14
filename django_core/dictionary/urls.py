from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/list', AlbumAPIView.as_view())
]