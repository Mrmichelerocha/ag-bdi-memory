from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from . import views
from .views import *

router = routers.DefaultRouter()
router.register('goal', goal_view_set, basename='goal')
router.register('obstacle', obstacle_view_set, basename='obstacle')
router.register('robot', robot_view_set, basename='robot')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]

