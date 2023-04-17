from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView

from apps.psychologist.models import Psychologist
from apps.psychologist.forms import PsychologistForm

from .blogs import Blog

class PsychologistListView(ListView):
    model = Psychologist
    queryset = model.objects.filter(active=True)
    template_name = "list_psychologist.html"


class PsychologistDetailView(DetailView):
    model = Psychologist
    slug_field = 'slug'
    template_name = 'detail_psychologist.html'


class AddFormPsychologist(View):
    def post(self, request):
        if request.method == "POST":
            form = PsychologistForm(request.POST)
            if form.is_valid():
                form.save(commit=False)
                form.save()
            return redirect('finish-post')
        

class BeforeAddPost(View):
    def get(self, request):
        return render(request, 'add-post.html', locals())




# Blogs
class BlogListView(ListView):
    model = Blog
    queryset = model.objects.all()
    template_name = "blogs-list.html"


class BlogDetailView(DetailView):
    model = Blog
    slug_field = 'slug'
    template_name = "detail-blog.html"



