from django import forms

from apps.psychologist.models import Psychologist


class PsychologistForm(forms.ModelForm):
    image = forms.ImageField()
    
    class Meta:
        model = Psychologist
        # fields = (
        #     'image', 
        #     'surname', 
        #     'name', 
        #     'country', 
        #     'sex', 
        #     'brief_description_work',
        #     'bio', 
        #     'education', 
        #     'email', 
        #     'status', 
        #     'main_specialization', 
        #     'additional_specialization_one',
        #     'online_consultation',
        #     'cost_of_online_consultation',
        #     'personal_reception',
        #     'cost_of_personal_reception',
        #     'phone',
        #     'skype',
        #     'instagram',
        #     'facebook',
        #     'twitter',
        # )

        fields = "__all__"
        exclude = ('active', 'slug',)