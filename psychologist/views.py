from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from apps.psychologist.models import Psychologist
from apps.psychologist.forms import PsychologistForm

class PsychologistListView(ListView):
    model = Psychologist
    queryset = model.objects.filter(active=True)
    template_name = "list_psychologist.html"


