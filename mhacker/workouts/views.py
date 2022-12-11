from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from .models import Workout_actual, Exercise, User
from .forms import MyUserCreationForm

class HomeView(generic.ListView):
    template_name = 'workouts/home.html'
    site_title = "Home Page"
    context_object_name = 'exercises'
    user = User.objects

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
    template_name = 'workouts/exercises.html'
    site_title = "Exercise Details"

    try:
        singleExercise = Exercise.objects.get(id=exercise_id)
    except Exercise.DoesNotExist:
        raise Http404("Exercise does not exist.")

    site_title = singleExercise.name
    context = {
        'exercise':singleExercise, 
        'exercises':exercises, 
        'site-title':site_title,
        'user':request.user,
    }
    
    return render(request, template_name, context)


@login_required(login_url='loginPage')
def workoutPage(request):
    template_name = 'workouts/workout_page.html'
    page = "workoutPage"
    site_title = "Workouts"
    user = request.user
    
    # pulls workouts for the logged in user
    try:
        user_workouts = Workout_actual.objects.filter(id=user.id)
    except Workout_actual.DoesNotExist:
        raise messages.error(request, "No workouts available")

    context = {
        'site_title':site_title,
        'page':page,
        'user_workouts':user_workouts,
        'username':User.get_username(request.user),
    }
    return render(request, template_name, context)
    
@login_required(login_url='loginPage')
def workoutAdd(request):
    template_name = 'workouts/addWorkout.html'
    page = "addWorkout"
    site_title = "Add Workout"

    if request.method == 'POST':
        workoutInfo = {
            'exercise':request.POST.get('exercise'),
            'number_of_sets':request.POST.get('number_of_sets'),
            'reps_per_set':request.POST.get('reps_per_set'),
            'weight_lifted_lbs':request.POST.get('weight_lifted_lbs'),
        }
        w = Workout_actual(
            exercise=workoutInfo.get('exercise'),
            number_of_sets=workoutInfo.get('number_of_sets'),
            reps_per_set=workoutInfo.get('reps_per_set'),
            weight_lifted_lbs=workoutInfo.get('weight_lifted_lbs'),
            time_of_workout=timezone.now()
            )
        w.save()
        return redirect('workoutPage')

    context = {
        'page':page, 
        'site_title':site_title,
    }
    return render(request, template_name, context)


def loginPage(request):
    page = 'login'
    template_name = 'workouts/login_login.html'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password is incorrect')
            

    context = {
        'page':page,
    }
    return render(request, template_name, context)

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.password1 is form.password2:
            if form.is_valid():
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'An error occurred during registration.')
                if form.data is None:
                    messages.error(request, 'Form has no data.')
                if form.errors is not None:
                    messages.error(request, form.errors)
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, 'workouts/login_register.html', {'form': form})

def logoutUser(request):
    logout(request)
    return redirect('home')