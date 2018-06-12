from rest_framework import serializers
from blogs.models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
	# Converts to JSON
	# Validates Data
	class Meta:
		model = BlogPost
		fields = ['id','user','title','content','timestamp']
