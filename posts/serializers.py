from rest_framework import serializers
from .models import Post, Vote

class PostSerializer(serializers.ModelSerializer):
    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')
    # create an variable that will grab the votes from the serializer
    votes = serializers.SerializerMethodField()
    class Meta:
        # tell what model to use
        model = Post
        # define the fields that you would like to serialize.  - add the votes to be displayed as well
        fields = ['id','title','url','poster','poster_id','created','votes']
    
    # then create an function to display the information - name function same name of variable above  get_variableName()
    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()




class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        # tell what model to use
        model = Vote
        # define the fields that you would like to serialize.
        fields = ['id']