"""mhacker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

# app_name = 'workouts'
urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('login/', views.loginPage, name="loginPage"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="registerPage"),
    path('exercises/', views.ExercisesView.as_view(), name="exercises"),
    path('exercises/<int:exercise_id>/', views.SingleExerciseView, name="singleExercise"),
    
    path('workoutpage/', views.workoutPage, name="workoutPage"),
    path('workout/Add-Workout/', views.addWorkout, name="addWorkout"),
    path('workout/update-workout/<int:workout_id>/', views.updateWorkout, name="updateWorkout"),
    path('workout/delete-workout/<int:workout_id>/', views.deleteWorkout, name="deleteWorkout"),
]