from rest_framework import serializers
from .models import *

class AlbumSerializer(serializers.ModelSerializer):
    words = serializers.StringRelatedField(many=True)

    class Meta:
        model = Person
        fields = ['telegram_id', 'words']