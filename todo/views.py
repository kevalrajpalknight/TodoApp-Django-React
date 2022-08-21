from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Task.objects.all()

