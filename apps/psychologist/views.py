from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import DetailView, ListView, CreateView

from apps.psychologist.models import Psychologist
from apps.psychologist.forms import PsychologistForm

from .blogs import Blog
from django.urls import reverse_lazy

class PsychologistListView(ListView):
    model = Psychologist
    queryset = model.objects.filter(active=True)
    template_name = "list_psychologist.html"


class PsychologistDetailView(DetailView):
    model = Psychologist
    slug_field = 'slug'
    template_name = 'detail_psychologist.html'


class HomePage(View):
    def get(self, request):
        return render(request, 'index.html', locals())



# Blogs
class BlogListView(ListView):
    model = Blog
    queryset = model.objects.all()
    template_name = "blogs-list.html"


class BlogDetailView(DetailView):
    model = Blog
    slug_field = 'slug'
    template_name = "detail-blog.html"

def CreateViewFunction(reqeust):
    if reqeust.method == "POST":
        surname = reqeust.POST['surname']
        name = reqeust.POST['name']
        country = reqeust.POST['country']
        sex = reqeust.POST['sex']
        brief_description_work = reqeust.POST['brief_description_work']
        bio = reqeust.POST['bio']
        education = reqeust.POST['education']
        status = reqeust.POST['status']
        main_specialization = reqeust.POST['main_specialization']
        additional_specialization_one = reqeust.POST['additional_specialization_one']
        online_consultation = reqeust.POST['online_consultation']
        cost_of_online_consultation = reqeust.POST['cost_of_online_consultation']
        personal_reception = reqeust.POST['personal_reception']
        cost_of_personal_reception = reqeust.POST['cost_of_personal_reception']
        phone = reqeust.POST['phone']
        skype = reqeust.POST['skype']
        instagram = reqeust.POST['instagram']
        facebook = reqeust.POST['facebook']
        twitter = reqeust.POST['twitter']

        Psychologist.objects.create(surname=surname, name=name, country=country, sex=sex, brief_description_work=brief_description_work,
                                    bio=bio, education=education, status=status, main_specialization=main_specialization, 
                                    additional_specialization_one=additional_specialization_one,
                                    online_consultation=online_consultation,
                                    cost_of_online_consultation=cost_of_online_consultation,
                                    personal_reception=personal_reception,
                                    cost_of_personal_reception=cost_of_personal_reception,
                                    phone=phone,
                                    skype=skype,
                                    instagram=instagram,
                                    facebook=facebook,
                                    twitter=twitter)
        return redirect('finish_form')


def ViewFormFunction(request):
    return render(request, 'add-form-psy.html', locals())


def FinishViewForm(request):
    return render(request, 'finish_form.html', locals())

