from django.contrib import admin
from apps.psychologist.models import Psychologist, AdditionalSpecialization, MainSpecialization, PsychologistStatus


class PsychologistAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name", )}


admin.site.register(Psychologist, PsychologistAdmin)
admin.site.register(AdditionalSpecialization)
admin.site.register(MainSpecialization)
admin.site.register(PsychologistStatus)