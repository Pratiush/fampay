from rest_framework import serializers
from .models import videoEntity

class VideoSerializer(serializers.ModelSerializer):
	class Meta:
		model = videoEntity
		fields = ['title','description','pub_date','thumbnail_url']
