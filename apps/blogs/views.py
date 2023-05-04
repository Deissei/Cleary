from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.blogs.models import Blog
from apps.homepage.models import SettingsHomePage

# Blogs
class BlogListView(ListView):
    model = Blog
    queryset = model.objects.all()
    template_name = "blogs/blogs-list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingsHomePage.objects.get(id=1)


class BlogDetailView(DetailView):
    model = Blog
    slug_field = 'slug'
    template_name = "blogs/blog-detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['setting'] = SettingsHomePage.objects.get(id=1)