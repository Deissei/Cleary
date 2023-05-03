from django.urls import path

from apps.blogs.views import BlogDetailView, BlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<str:slug>/', BlogDetailView.as_view(), name='blog_detail'),
]
