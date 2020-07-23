from rest_framework import serializers
from .models import GEOPoint, File


class GEOPointSerialize(serializers.ModelSerializer):
    class Meta:
        model = GEOPoint
        fields = ['name', 'lat', 'lng']


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file', 'remark', 'timestamp')