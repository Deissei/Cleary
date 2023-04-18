from django.urls import path, include

from .views import HomePage, PsychologistListView, BlogListView, ViewFormFunction, CreateViewFunction, FinishViewForm


urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('psychologits/', PsychologistListView.as_view(), name='list_psycholog'),
    path('blogs/', BlogListView.as_view(), name='blog_list'),
    path('completion-form/', ViewFormFunction, name='view_form_function'),
    path('completion-form-add/', CreateViewFunction, name='compl_form'),
    path('finish/', FinishViewForm, name='finish_form')
]
