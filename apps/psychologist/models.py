from django.db import models
from django.urls import reverse


class AdditionalSpecialization(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Дополнительная специалиция"


class MainSpecialization(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Основная Специализации"


class PsychologistStatus(models.Model):
    """Модель статуса психолога"""
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Статус Психологи"


class Psychologist(models.Model):
    """Модель Психолога"""
    active = models.BooleanField(null=True, blank=True)
    image = models.ImageField(upload_to='psychologist')
    
    SEX_CHOICES = [
        ("М", "Мужской" ),
        ("Ж", "Женский" ),
    ]
    online_consultation_CHOICES = [
        ('Д', 'Да'),
        ('Н', 'Нет'),
    ]
    surname = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    sex = models.CharField(max_length=7, choices=SEX_CHOICES)
    brief_description_work = models.CharField(max_length=500)
    bio = models.TextField()
    education = models.TextField()

    status = models.ForeignKey(PsychologistStatus, on_delete=models.SET_DEFAULT, default='None')
    main_specialization = models.ForeignKey(MainSpecialization, on_delete=models.SET_DEFAULT, default='None')
    
    additional_specialization_one = models.ForeignKey(AdditionalSpecialization, on_delete=models.SET_DEFAULT, default='None', null=True, blank=True)
    # additional_specialization_two = models.ForeignKey(AdditionalSpecialization, on_delete=models.SET_DEFAULT, default='None', null=True, blank=True)
    # additional_specialization_three = models.ForeignKey(AdditionalSpecialization, on_delete=models.SET_DEFAULT, default='None', null=True, blank=True)

    online_consultation = models.CharField(max_length=3, choices=online_consultation_CHOICES)
    cost_of_online_consultation = models.IntegerField(help_text='руб', null=True, blank=True)

    personal_reception = models.CharField(max_length=3, choices=online_consultation_CHOICES) 
    cost_of_personal_reception = models.IntegerField(help_text='руб', null=True, blank=True)

    address_of_the_reception_room = models.CharField(max_length=500, null=True, blank=True)

    phone = models.CharField(max_length=20)
    # social
    skype = models.CharField(max_length=100, null=True, blank=True)
    instagram = models.CharField(max_length=100, null=True, blank=True)
    facebook = models.CharField(max_length=100, null=True, blank=True)
    twitter = models.CharField(max_length=100, null=True, blank=True)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.surname}-{self.name}"
    

    def get_absolute_url(self):
        return reverse("psychologist_detail", kwargs={"slug": self.slug})


    class Meta:
        verbose_name_plural = "Психологи"