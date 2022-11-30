import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

class Exercise:
    muscles = 
    equipment
    aType

class workout_goal:
    num_Sets = 
    reps_per_set =
    weight_lifted = 
    duration =
    avg_speed =
    distance_traveled =

class workout_actual:
    num_Sets = 
    reps_per_set =
    weight_lifted = 
    duration =
    avg_speed =
    distance_traveled =
    goal_met = False

class workout_day:
    actual_workout = workout_actual
    goal_workout = workout_goal
    date = datetime.date()
    time_start = datetime.now() - 1 hour
    time_end = datetime.now()


    goals_met_sum = goalCompletion(actual_workout,goal_workout)
    goal_avg = goals_met_sum / len(goal_workout)
    
    def goalCompletion(actual,goal):
        goalSum = 0
        for i in actual.goal_met:
            if i: goalSum++

        goal_avg = goalSum/len(goal)

class Week:

class Plan: