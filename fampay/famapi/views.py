from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import videoEntity
from .serializers import VideoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
# Create your views here.


@api_view(['GET'])
def healthCheck(request):
	return Response("Health Check successful",status=status.HTTP_200_OK)

class VideoPagination(PageNumberPagination):
	page_size = 3
	page_size_query_param = 'page_size'
	max_page_size = 6


class VideoViewSet(viewsets.ModelViewSet):
	queryset = videoEntity.objects.all().order_by('-pub_date')
	serializer_class = VideoSerializer
	pagination_class = VideoPagination
