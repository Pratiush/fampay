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
from background_task import background
import requests
import json
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



@background(schedule=10)
def GetVideos():
	url = 'https://www.googleapis.com/youtube/v3/search/'
	params = {
		'part' :'snippet',
		'q' : 'song',
		'publishedAfter' : '2020-04-27T00:00:00Z',
		'maxResults' : '10',
		'key' : 'AIzaSyD3ZNIItpxhxDj5EPpQ5GpEIo4fhvLL2d8',
	}

	response = requests.get(url,params=params)
	response = response.json()['items']
	#print(response)
	video_list = []
	for i in range(0,len(response)):
		videoDetail = response[i]['snippet']
		video_list.append(videoEntity.create(title=videoDetail['title'],description=videoDetail['description'],pub_date=videoDetail['publishedAt'],thumbnail_url=videoDetail['thumbnails']['medium']['url']))
	print(video_list)
	videoEntity.objects.bulk_create(video_list) #save in db
	print("Saved new videos in database")

def backgroundTask(request):
	GetVideos(repeat=50) # get videos every 50+10 sec
	return HttpResponse("Background task for pulling latest videos from youtube scheduled.")

