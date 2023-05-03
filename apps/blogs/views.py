from django.shortcuts import render
from django.views.generic import ListView, DetailView

from apps.blogs.models import Blog


# Blogs
class BlogListView(ListView):
    model = Blog
    queryset = model.objects.all()
    template_name = "blogs/blogs-list.html"


class BlogDetailView(DetailView):
    model = Blog
    slug_field = 'slug'
    template_name = "blogs/blog-detail.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['']