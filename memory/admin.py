from django.contrib import admin
from memory.models import modelo_memory_obstacle, modelo_memory_goal, modelo_memory_robot

# Register your models here.
class memory_goal(admin.ModelAdmin):
    pass
admin.site.register(modelo_memory_goal, memory_goal)

# Register your models here.
class memory_obstacle(admin.ModelAdmin):
    pass
admin.site.register(modelo_memory_obstacle, memory_obstacle)

# Register your models here.
class memory_robot(admin.ModelAdmin):
    pass
admin.site.register(modelo_memory_robot, memory_robot)