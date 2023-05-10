from django.shortcuts import redirect, render
from django.views.generic import CreateView

from django.urls import reverse_lazy

from apps.psychologist.models import Psychologist
from utils.send_message import send_email
from apps.makeIN.forms import MakeAnAppointmentForm
from apps.makeIN.models import MakeAnAppointment

from apps.homepage.models import SettingsHomePage


def CreateViewFunction(reqeust):
    if reqeust.method == "POST":
        surname = reqeust.POST['surname']
        name = reqeust.POST['name']
        image = reqeust.POST['image']
        country = reqeust.POST['country']
        sex = reqeust.POST['sex']
        brief_description_work = reqeust.POST['brief_description_work']
        bio = reqeust.POST['bio']
        education = reqeust.POST['education']
        email = reqeust.POST['email']
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

        Psychologist.objects.create(image=image, surname=surname, name=name, country=country, sex=sex, brief_description_work=brief_description_work,
                                    bio=bio, education=education, email=email, status=status, main_specialization=main_specialization, 
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
        
        print("[!]SENDING MESSAGE")
        send_email(f"{name} Заполнил форму!", f"Здравье желаю мой повелитель!\nТУТ какойто чел отправил форму, говорит что сильный психолог!\nВот его данные:\nИмя: {name}\nФамилия: {surname}\nЕмаил: {email}\n\nПолностью можете посмотреть переходя по ссылке\n\nhttp://127.0.0.1:8000/admin/psychologist/psychologist/")
        print("[!]SEND MESSAGE")
        return redirect('finish_form')


def ViewFormFunction(request):
    setting = SettingsHomePage.objects.get(id=1)
    return render(request, 'forms/add-form-psy.html', locals())


def FinishViewForm(request):
    setting = SettingsHomePage.objects.get(id=1)
    return render(request, 'forms/finish_form.html', locals())


def CreateMakeAnAppointmentFunction(request):
    if request.method == "POST":
        form = MakeAnAppointmentForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('homepage')
        return redirect('homepage')


class CreateMakeAnAppointmentFunction(CreateView):
    model = MakeAnAppointment
    form_class = MakeAnAppointmentForm
    template_name = "homepage/index.html"
    success_url = reverse_lazy("homepage")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingsHomePage.objects.get(id=1)
        return context
