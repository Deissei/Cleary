from django import forms
from apps.psychologist.models import Psychologist


class PsychologistForm(forms.ModelForm):
    """Форма для псхологов"""
    class Meta:
        model = Psychologist
        fields = (
            'surname',
            'name',
            'country',
            'sex',
            'brief_description_work',
            'bio',
            'education',
            'status',
            'main_specialization',
            'additional_specialization_one',
            'online_consultation',
            'cost_of_online_consultation',
            'personal_reception',
            'cost_of_personal_reception',
            'address_of_the_reception_room',
            'phone',
            'skype',
            'instagram',
            'twitter',
        )
