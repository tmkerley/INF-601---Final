from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic
from .models import Workout_actual, Exercise, User

class HomeView(generic.ListView):
    template_name = 'workouts/home.html'
    site_title = "Home Page"
    context_object_name = 'exercises'

    def get_queryset(self):
        
        # Return the exercise objects
        return Exercise.objects.all()[:5]

class ExercisesView(generic.ListView):
    template_name = "workouts/exercises.html"
    site_title = "Exercises"
    context_object_name = 'exercises'

    def get_queryset(self):
        
        # Return the exercise objects
        return Exercise.objects.all()[:5]

def SingleExerciseView(request, exercise_id):
    exercises = Exercise.objects.all()
    template_name = 'workouts/exercise.html'
    site_title = "Exercise Details"

    try:
        singleExercise = Exercise.objects.get(id=exercise_id)
    except Exercise.DoesNotExist:
        raise Http404("Exercise does not exist.")

    site_title = singleExercise.name

    return render(
        request, 
        'workouts/exercises.html',
        {'exercise':singleExercise, 'exercises':exercises, 'site-title':site_title})


@login_required
def Workout_View(request):
    template_name = "workouts/workouts.html"
    site_title = "Workouts"
    user_workouts = Workout_actual.objects.filter(User.id)
    return render(request, template_name,
        {'user_workouts':user_workouts})
    

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

def logoutUser(request):
    logout(request)
    return redirect('home')

""" 
TODO Modify this to match mine. Add template and form function
def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')

    return render(request, 'base/login_register.html', {'form': form}) """