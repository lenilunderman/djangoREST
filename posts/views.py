from django.shortcuts import render
# imports related to rest_framework
from rest_framework import generics
# import of the .models, table Post
from .models import Post
# import the serializer class to be used
from .serializers import PostSerializer
# Create your views here.
class PostList(generics.ListAPIView):
    # display all the posts using query set
    queryset = Post.objects.all()
    # tell what serializer to use for this class
    serializer_class = PostSerializer