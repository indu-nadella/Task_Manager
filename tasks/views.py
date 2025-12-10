# from django.shortcuts import render
from rest_framework import generics,viewsets,permissions
from django.contrib.auth.models import User,Group
from tasks.serializers import UserRegisterSerializer,TaskSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from tasks.models import TaskModel
from tasks.permissions import IsAdminOrOwner

# Create your views here.
class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserRegisterSerializer
    permission_classes=[AllowAny]

class TaskView(viewsets.ModelViewSet):
    serializer_class=TaskSerializer
    queryset=TaskModel.objects.all()
    permission_classes=[permissions.IsAuthenticated,IsAdminOrOwner]
    
    def get_queryset(self):
        user=self.request.user
        if user.groups.filter(name='Admin').exists():
            return TaskModel.objects.all()
        return TaskModel.objects.filter(owner=user)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)