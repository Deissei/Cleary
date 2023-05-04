from django.urls import path, include

from .views import (
    HomePage, 
    PsychologistListView, 
    PsychologistDetailView, 
    PsychologistCreateView
)


urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('psychologits/', PsychologistListView.as_view(), name='list_psycholog'),
    path('psychologits/<str:slug>', PsychologistDetailView.as_view(), name='psychologist_detail'),
    path('create-psychologist/', PsychologistCreateView.as_view(), name='__create'),
]
