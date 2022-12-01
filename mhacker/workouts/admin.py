from django.contrib import admin

from .models import Exercise

class ExerciseListAdmin(admin.TabularInline):
    name = Exercise.name
    muscles = Exercise.muscles
    equipment = Exercise.equipment
    aType = Exercise.aType

admin.site.register(Exercise, ExerciseListAdmin)