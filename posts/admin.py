from django.contrib import admin
# Get the models that you would like to register on the admin
from .models import Post, Vote
# Register your models here.
admin.site.register(Post)
admin.site.register(Vote)