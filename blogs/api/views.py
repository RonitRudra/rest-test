from django.shortcuts import render
from rest_framework import generics
from blogs.models import BlogPost 
from blogs.api.serializers import BlogPostSerializer
# Create your views here.

class BlogPostRUDView(generics.RetrieveUpdateDestroyAPIView):
	lookup_field = 'pk'
	queryset = BlogPost.objects.all()
	serializer_class = BlogPostSerializer