from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class TodoModelViewSet(ModelViewSet):
    # crud set
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    