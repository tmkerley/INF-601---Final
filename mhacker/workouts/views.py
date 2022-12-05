from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import generic
from .models import Workout_actual, Exercise, User

class HomeView(generic.ListView):
    template_name = 'workouts/home.html'
    site_title = "Home Page"
    exercises = Exercise.objects.all()

    def get_queryset(self):
        
        # Return the exercise objects
        return Exercise.objects.all()
        """ return Workout_actual.objects.filter(
            date_lifted__lte=timezone.now()).order_by('date_lifted')[:10] """

class ExercisesView(generic.ListView):
    template_name = "workouts/exercises.html"
    site_title = "Exercises"
    exercises = Exercise.objects

    def get_queryset(self):
        
        # Return the exercise objects
        return Exercise.objects

@login_required
class Workout_PlanView(generic.ListView):
    template_name = "workouts/workout_plan"
    site_title = "Workout Plan"
    pass

def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Username OR password is incorrect')

    context = {'page':page}
    return render(request, 'workouts/login_register.html', context)