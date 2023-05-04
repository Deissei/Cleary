from django.forms import ModelForm

from apps.makeIN.models import MakeAnAppointment


class MakeAnAppointmentForm(ModelForm):
    class Meta:
        model = MakeAnAppointment
        fields = "__all__"
