from django.db import models
# Create your models here.

class modelo_memory_robot(models.Model):
    _class = models.CharField(max_length=100)
    _x = models.FloatField()
    _y = models.FloatField()
    
class modelo_memory_obstacle(models.Model):
    _class = models.CharField(max_length=100)
    _x = models.FloatField()
    _y = models.FloatField()
    
class modelo_memory_goal(models.Model):
    _class = models.CharField(max_length=100)
    _x = models.FloatField()
    _y = models.FloatField()
    
