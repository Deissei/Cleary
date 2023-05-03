from django.contrib import admin

from apps.blogs.models import Blog


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title", )}

admin.site.register(Blog, BlogAdmin)
