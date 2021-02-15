from django.shortcuts import render
# imports related to rest_framework
from rest_framework import generics, permissions, mixins, status
# import the error validation from rest
from rest_framework.exceptions import ValidationError
# import the response to be used inside the delete part of the api
from rest_framework.response import Response
# import of the .models, table Post
from .models import Post, Vote
# import the serializer class to be used
from .serializers import PostSerializer, VoteSerializer

# Create your views here.
class PostList(generics.ListCreateAPIView):
    # display all the posts using query set
    queryset = Post.objects.all()
    # tell what serializer to use for this class
    serializer_class = PostSerializer
    # import permissions from the rest framework.
    # that allow users to see the info if they are not loged in or write if they are loged in
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Create the function and use the special name 'perform_create
    def perform_create(self, serializer):
        serializer.save(poster=self.request.user)

class VoteCreate(generics.CreateAPIView, mixins.DestroyModelMixin):
    # display all the posts using query set
    queryset = Post.objects.all()
    # tell what serializer to use for this class
    serializer_class = VoteSerializer
    # import permissions from the rest framework.
    # someone has to be authenticated to read this
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    # Create the function and use the special name 'perform_create
    def perform_create(self, serializer):
        # check if something came back from the queryset
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post.')
        serializer.save(voter=self.request.user, post=Post.objects.get(pk=self.kwargs['pk']))

    # Create the function to delete one vote
    def delete(self, request, *args, **kwargs):
        if self.get_queryset().exists():
            self.get_queryset().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            raise ValidationError('You never voted for this post.')
