from rest_framework import serializers
from .models import GEOPoint


class GEOPointSerialize(serializers.ModelSerializer):
    class Meta:
        model = GEOPoint
        fields = ['name', 'lat', 'lng']
