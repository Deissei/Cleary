from django.urls import path

from apps.makeIN.views import (
    ViewFormFunction,
    CreateViewFunction,
    FinishViewForm,
    CreateMakeAnAppointmentFunction
)

urlpatterns = [
    path('completion-form/', ViewFormFunction, name='view_form_function'),
    path('completion-form-add/', CreateViewFunction, name='compl_form'),
    path('finish/', FinishViewForm, name='finish_form'),
    path('create_make/', CreateMakeAnAppointmentFunction.as_view(), name="create_make")
]
