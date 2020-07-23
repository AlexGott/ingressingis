import logging

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from rest_framework_xml.parsers import XMLParser

from .models import GEOPoint
from .serializers import GEOPointSerialize, FileSerializer

logger = logging.getLogger(__name__)


class GEOPointView(APIView):
    """API для работы с геоточками"""
    def get(self, request):
        portal = GEOPoint.objects.all()
        serializer = GEOPointSerialize(portal, many=True)
        return Response({'data': serializer.data})


class FileDownload(APIView):
    """Загрузка файлов"""
    parser_classes = (FileUploadParser,)

    def post(self, request, format=None):
        file_obj = request.FILES['file']
        logger.info(file_obj)
        return Response({'received data': request.DATA})


class FileView(APIView):

    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

