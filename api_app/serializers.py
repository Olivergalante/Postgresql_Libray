from rest_framework import serializers
from .models import Libray


class LibraySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Libray
        fields = ['title', 'author', 'description']
