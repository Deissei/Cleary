from django.contrib import admin
from apps.psychologist.models import Psychologist, AdditionalSpecialization, MainSpecialization, PsychologistStatus

from .blogs import Blog

class PsychologistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Psychologist, PsychologistAdmin)
admin.site.register(AdditionalSpecialization)
admin.site.register(MainSpecialization)
admin.site.register(PsychologistStatus)
admin.site.register(Blog, BlogAdmin)