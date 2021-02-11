from rest_framework import serializers
from .models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    class Meta:
        # tell what model to use
        model = Post
        # define the fields that you would like to serialize.
        fields = ['id','title','url','poster','poster_id','created']


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        # tell what model to use
        model = Vote
        # define the fields that you would like to serialize.
        fields = ['id']