from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Exercise, Workout_actual # Workout_goal

class ExerciseListAdmin(admin.TabularInline):
    name = Exercise.name
    muscles = Exercise.muscles
    equipment = Exercise.equipment
    aType = Exercise.aType

class WorkoutActualListAdmin(admin.TabularInline):
    user = Workout_actual.user
    # goal_workout_id = Workout_actual.goal_workout_id
    time_of_workout = Workout_actual.time_of_workout

    goal_met = Workout_actual.goal_met
    exercise = Workout_actual.exercise
    number_of_sets = Workout_actual.number_of_sets
    reps_per_set = Workout_actual.reps_per_set
    weight_lifted_lbs = Workout_actual.weight_lifted_lbs
    # duration stored in seconds
    duration_seconds = Workout_actual.duration_seconds
    # speed is recorded in mph
    average_speed_mph = Workout_actual.average_speed_mph
    # distance is record in miles
    miles_traveled = Workout_actual.miles_traveled

""" class WorkoutGoalListAdmin(admin.TabularInline):
    user = Workout_goal.user
    exercise = Workout_goal.exercise
    number_of_sets = Workout_goal.number_of_sets
    reps_per_set = Workout_goal.reps_per_set
    weight_lifted_lbs = Workout_goal.weight_lifted_lbs
    # time should be hh:mm:ss
    duration_seconds = Workout_goal.duration_seconds
    # speed is recorded in mph
    average_speed_mph = Workout_goal.average_speed_mph
    # distance is record in miles
    miles_traveled = Workout_goal.miles_traveled """

admin.site.register(Exercise)
admin.site.register(Workout_actual)
# admin.site.register(Workout_goal)