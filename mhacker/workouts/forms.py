from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Workout_actual


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class workoutForm(ModelForm):
    class Meta:
        model = Workout_actual
        fields = [
            'exercise',
            'number_of_sets',
            'reps_per_set',
            'weight_lifted_lbs',
        ]

    def clean_exercise(self):
        exercise = self

    def clean_weight(self):
        weight = self