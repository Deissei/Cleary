from django.urls import path, include

from .views import (
    HomePage, 
    PsychologistListView, 
    PsychologistDetailView
)


urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('psychologits/', PsychologistListView.as_view(), name='list_psycholog'),
    path('psychologits/<str:slug>', PsychologistDetailView.as_view(), name='psychologist_detail'),
]
