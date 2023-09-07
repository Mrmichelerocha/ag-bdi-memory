from django.shortcuts import render
from memory.serializer import serializer_goal, serializer_obstacle, serializer_robot
from memory.models import modelo_memory_obstacle, modelo_memory_goal, modelo_memory_robot
from rest_framework import viewsets

# Create your views here.
class goal_view_set(viewsets.ModelViewSet):
    queryset = modelo_memory_goal.objects.all()
    serializer_class = serializer_goal
    
class robot_view_set(viewsets.ModelViewSet):
    queryset = modelo_memory_robot.objects.all()
    serializer_class = serializer_robot
    
class obstacle_view_set(viewsets.ModelViewSet):
    queryset = modelo_memory_obstacle.objects.all()
    serializer_class = serializer_obstacle
    