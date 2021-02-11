from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        # tell what model to use
        model = Post
        # define the fields that you would like to serialize.
        fields = ['id','title','url','poster','created']
