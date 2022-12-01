from django.views import generic
from django.utils import timezone
from .models import Workout_actual

class IndexView(generic.ListView):
    template_name = 'workouts/index.html'
    site_title = "User Home Page"
    
    def get_queryset(self):
        """
        Return the last 10 workouts performed
        """
        return Workout_actual.objects.filter(
            date_lifted__lte=timezone.now()).order_by('date_lifted')[:10]
    
class ExerciseView(generic.ListView):
    pass

class Workout_PlanView(generic.ListView):
    pass
