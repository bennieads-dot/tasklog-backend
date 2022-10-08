from django.shortcuts import render
from rest_framework import generics
from api.models import Priority, Group, Task
from api.serializers import PrioritySerializer, GroupSerializer, TaskSerializer


# Create your views here.
class PriorityList(generics.ListCreateAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer


class PriorityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer


class GroupList(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
