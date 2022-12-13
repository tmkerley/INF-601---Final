from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.views import generic
from django.utils import timezone
from .models import Workout_actual, Exercise, User, Days_plan
from .forms import MyUserCreationForm, workoutForm

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
    # pulls a single exercise to show it's details and instruction
    try:
        singleExercise = Exercise.objects.get(id=exercise_id)
    except Exercise.DoesNotExist:
        raise Http404("Exercise does not exist.")

    context = {
        'exercise':singleExercise, 
        'exercises':Exercise.objects.all(), 
        'site-title':singleExercise.name,
        'user':request.user,
    }
    
    return render(request, 'workouts/exercises.html', context)

@login_required(login_url='loginPage')
def workoutPage(request):
    # pulls workouts for the logged in user
    try:
        user_workouts = Workout_actual.objects.filter(user=request.user)
    except Workout_actual.DoesNotExist:
        raise messages.error(request, "No workouts available")

    context = {
        'site_title':"Workouts",
        'page':"workoutPage",
        'user_workouts':user_workouts,
        'username':request.user,
    }
    return render(request, 'workouts/workout_page.html', context)
    
@login_required(login_url='loginPage')
def addWorkout(request):
    # shows the empty form
    form = workoutForm()

    # if the submit hit, create new entry into database
    if request.method == 'POST':
        Workout_actual.objects.create(
            user = request.user,
            exercise = Exercise.objects.get(id=request.POST["exercise"]),
            reps_per_set = request.POST["reps_per_set"],
            weight_lifted_lbs = request.POST["weight_lifted_lbs"],
            number_of_sets = request.POST["number_of_sets"],
        )
        return redirect('workoutPage')
    else:
        messages.error(request, "Workout not added.")

    context = {
        'page':"addWorkout", 
        'site_title':"Add Workout",
        'form':form,
    }
    return render(request, 'workouts/workoutform.html', context)

@login_required(login_url='loginPage')
def updateWorkout(request, workout_id):
    # fills the form witht he selected workout
    selectWorkout = Workout_actual.objects.get(id=workout_id)
    form = workoutForm(instance=selectWorkout)

    # if the submit hit, updates entry into database
    if request.method == 'POST':
        selectWorkout.exercise = Exercise.objects.get(id=request.POST["exercise"])
        selectWorkout.reps_per_set = request.POST["reps_per_set"]
        selectWorkout.weight_lifted_lbs = request.POST["weight_lifted_lbs"]
        selectWorkout.number_of_sets = request.POST["number_of_sets"]
        selectWorkout.save()
        return redirect('workoutPage')

    context = {
        'page':"UpdateWorkout", 
        'site_title':"Update Workout",
        'form':form,
    }
    return render(request, 'workouts/workoutform.html', context)

@login_required(login_url='loginPage')
def deleteWorkout(request, workout_id):
    selectWorkout = Workout_actual.objects.get(id=workout_id)

    if request.method == 'POST':
        Workout_actual.objects.delete(
            id = workout.id,
        )
        return redirect('workoutPage')

    context = {
        'page':"DeleteWorkout", 
        'site_title':"Delete Workout",
        'form':form,
    }
    return render(request, 'workouts/workoutform.html', context)

@login_required
def planDisplay(request):
    user_workouts = Workout_actual.objects.filter(user=request.user)

    workout_of_the_day = Days_plan.getRecentPlan()
    context = {
        'page':"goals", 
        'site_title':"goals",
    }
    return render(request, 'workouts/goalsbase.html', context)

def loginPage(request):
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
        'page':'login',
    }
    return render(request, 'workouts/login_login.html', context)

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