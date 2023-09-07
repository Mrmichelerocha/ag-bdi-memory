from django.urls import path, include
from django.contrib.auth.models import User
from memory.models import modelo_memory_goal, modelo_memory_obstacle, modelo_memory_robot
from rest_framework import serializers

# Serializers define the API representation.
class serializer_obstacle(serializers.ModelSerializer):
    class Meta:
        model = modelo_memory_obstacle
        fields = '__all__'
    
# Serializers define the API representation.
class serializer_goal(serializers.ModelSerializer):
    class Meta:
        model = modelo_memory_goal
        fields = '__all__'    

# Serializers define the API representation.
class serializer_robot(serializers.ModelSerializer):
    class Meta:
        model = modelo_memory_robot
        fields = '__all__'    
