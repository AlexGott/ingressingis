from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .serializers import GEOPointSerialize
from .models import GEOPoint
from rest_framework.response import Response


class GEOPointView(APIView):
    def get(self, request):
        portal = GEOPoint.objects.all()
        serializer = GEOPointSerialize(portal,many=True)
        return Response({'data': serializer.data})
