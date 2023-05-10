from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import DetailView, ListView, CreateView

from django.urls import reverse_lazy

from apps.psychologist.models import Psychologist
from apps.psychologist.forms import PsychologistForm
from apps.homepage.models import SettingsHomePage

class PsychologistListView(ListView):
    model = Psychologist
    queryset = model.objects.filter(active=True)
    template_name = "psychologist/list_psychologist.html"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingsHomePage.objects.get(id=1)
        return context

class PsychologistDetailView(DetailView):
    model = Psychologist
    slug_field = 'slug'
    template_name = 'psychologist/psycholog-detail.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingsHomePage.objects.get(id=1)
        return context


class HomePage(View):
    def get(self, request):
        psychologists = Psychologist.objects.filter(active=True)
        setting = SettingsHomePage.objects.get(id=1)
        return render(request, 'homepage/index.html', locals())


class PsychologistCreateView(CreateView):
    model = Psychologist
    form_class = PsychologistForm
    template_name = "forms/add-form-psy.html"
    success_url = reverse_lazy('finish_form')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingsHomePage.objects.get(id=1)
        return context
