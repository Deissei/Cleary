from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import DetailView, ListView


from apps.psychologist.models import Psychologist


class PsychologistListView(ListView):
    model = Psychologist
    queryset = model.objects.filter(active=True)
    template_name = "psychologist/list_psychologist.html"


class PsychologistDetailView(DetailView):
    model = Psychologist
    slug_field = 'slug'
    template_name = 'psychologist/psycholog-detail.html'


class HomePage(View):
    def get(self, request):
        psychologists = Psychologist.objects.filter(active=True)
        return render(request, 'homepage/index.html', locals())
