import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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

class Exercise(models.Model):
    EXERCISE_TYPES = (
        ('AN', 'Anaerobic'),
        ('AR', 'Aerorobic'),
    )

    name = models.CharField(max_length=200)
    # TODO make muscles a separate table
    muscles = models.CharField(max_length=128)
    # TODO make equipment a separate table
    equipment = models.CharField(max_length=128)
    # anerobic vs aerobic types
    aType = models.CharField(max_length=16, choices=EXERCISE_TYPES)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return self.name

class Workout_goal(models.Model):
    user_id = models.ForeignKey(User.id, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    number_of_sets = models.IntegerField(default=3)
    reps_per_set = models.IntegerField(default=6)
    weight_lifted = models.IntegerField(default=10)
    # time should be hh:mm:ss
    duration_seconds = models.TimeField(default='00:12:30')
    # speed is recorded in mph
    average_speed_mph = models.FloatField(default=7.2)
    # distance is record in miles
    miles_traveled = models.FloatField(default=1.5)


class Workout_actual(models.Model):
    user_id = models.ForeignKey(User.id)
    goal_workout_id = models.ForeignKey(
        Workout_goal, on_delete=models.CASCADE)
    time_of_workout = models.DateField('time of workout')

    goal_met = models.BooleanField(default=False)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    number_of_sets = models.IntegerField(default=1)
    reps_per_set = models.IntegerField(default=1)
    weight_lifted = models.IntegerField(default=5)
    # time should be hh:mm:ss
    duration = models.TimeField(default='00:12:30')
    # speed is recorded in mph
    average_speed = models.FloatField(default=6.0)
    # distance is record in miles
    distance_traveled = models.FloatField(default=1.5)


    # counts how many goals were completed.
    def goalCompletion(self):
        if Workout_goal.number_of_sets == Workout_actual.number_of_sets:
            if Workout_goal.weight_lifted == Workout_actual.weight_lifted:
                if Workout_goal.reps_per_set == Workout_actual.reps_per_set:
                    return True

    # calculates the percentage of goals completed.
    def goalPercent(actual,goal):
        return goalCompletion(actual,goal) / len(goal)

    # 
    def was_performed_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(
            days=14) <= self.time_of_workout <= now

class Days_workout(models.Model):
    actual_workout = models.ForeignKey(Workout_actual, on_delete=models.CASCADE)
    goal_workout = models.ForeignKey(Workout_goal, on_delete=models.CASCADE)
    date_of_workouts = datetime.date
    met_day_goals = models.BooleanField(default=False)
    met_day_goals_percent = models.IntegerField(default=0)

    # counts how many goals were completed.
    def goalCompletion(actual,goal):
        goalSum = 0
        for i in actual.goal_met:
            if i: 
                goalSum += 1
        return goalSum

    # calculates the percentage of goals completed.
    def goalPercent(actual,goal):
        return goalCompletion(actual,goal) / len(goal)

"""
    met_day_goals_percent = goalCompletion(
        actual_workout,goal_workout) / len(goal_workout)    
    if met_day_goals_percent == 100:
        met_day_goals = True 
"""
        


    

class Weeks_plan(models.Model):
    pass
    """ num_days_workout = models.IntegerField(default=3)
    num_days_rest = models.IntegerField(default=(7-num_days_workout))
    week_num = models.IntegerField(default=0)
    met_week_goal = models.BooleanField(default=False)
    met_week_goal_percent = models.models.IntegerField(default=0) """


class Workout_Program(models.Model):
    pass