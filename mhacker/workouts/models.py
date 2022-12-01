import datetime
from django.db import models
from django.utils import timezone
from django.contrib import admin

def goalCompletion(actual,goal):
    goalSum = 0
    for i in actual.goal_met:
        if i: 
            goalSum += 1
    return goalSum

def goalPercent(actual,goal):
    goalSum = 0
    for i in actual.goal_met:
        if i: 
            goalSum += 1
    return goalSum/goal.goal_met

class Exercise:
    name = models.CharField(max_length=200)
    # TODO make muscles a separate table
    muscles = models.CharField(max_length=128)
    # TODO make equipment a separate table
    equipment = models.CharField(max_length=128)
    # anerobic vs aerobic types
    aType = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Workout_goal:
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    num_Sets = models.IntergerField(default=1)
    reps_per_set = models.IntergerField(default=1)
    weight_lifted = models.IntergerField(default=5)
    # time should be hh:mm:ss
    duration = models.TimeField(default='00:12:30')
    # speed is recorded in mph
    avg_speed = models.FloatField(default=7.2)
    # distance is record in miles
    distance_traveled = models.FloatField(default=1.5)
    date_lifted = models.DateField


class Workout_actual:
    num_Sets = models.IntergerField(default=1)
    reps_per_set = models.IntergerField(default=1)
    weight_lifted = models.IntergerField(default=5)
    # time should be hh:mm:ss
    duration = models.TimeField(default='00:12:30')
    # speed is recorded in mph
    avg_speed = models.FloatField(default=6.0)
    # distance is record in miles
    distance_traveled = models.FloatField(default=1.5)
    goal_met = models.BooleanField(default=False)
    date_lifted = models.DateField.auto_now(True)

    def goalCompletion(actual,goal):
        goalSum = 0
        for i in actual.goal_met:
            if i: 
                goalSum += 1
        return goalSum

    def goalPercent(actual,goal):
        goalSum = 0
        for i in actual.goal_met:
            if i: 
                goalSum += 1
        return goalSum/goal.goal_met

class workout_day:
    actual_workout = models.ForeignKey(workout_actual, on_delete=models.CASCADE)
    goal_workout = models.ForeignKey(workout_goal, on_delete=models.CASCADE)
    date = datetime.date()
    time_start = datetime.now()
    time_end = datetime.now()
    met_day_goals = models.BooleanField(default=False)
    met_day_goals_percent = models.IntegerField(default=0)

    def goalCompletion(actual,goal):
        goalSum = 0
        for i in actual.goal_met:
            if i: 
                goalSum += 1
        return goalSum

    def goalPercent(actual,goal):
        goalSum = 0
        for i in actual.goal_met:
            if i: 
                goalSum += 1
        return goalSum/goal.goal_met

    met_day_goals_percent = goalCompletion(
        actual_workout,goal_workout) / len(goal_workout)    
    if met_day_goals_percent == 100:
        met_day_goals = True
        


    

class Week:
    pass
    """ num_days_workout = models.IntegerField(default=3)
    num_days_rest = models.IntegerField(default=(7-num_days_workout))
    week_num = models.IntegerField(default=0)
    met_week_goal = models.BooleanField(default=False)
    met_week_goal_percent = models.models.IntegerField(default=0) """


class Plan:
    pass