from datetime import *
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets

# Post의 목록, detail 보여주기, 수정하기, 삭제하기 모두 가능
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
   
   	# serializer.save() 재정의
    def perform_create(self, serializer):
        serializer.save(user = self.request.user)