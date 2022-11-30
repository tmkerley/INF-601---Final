from django.http import HttpResponse
from django.views import generic
import datetime



class IndexView(generic.ListView):
    template_name = 'mysite/index.html'
    site_title = 'Main'

    def get_queryset(self):
        return