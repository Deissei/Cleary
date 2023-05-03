from django.db import models
from django.urls import reverse

from .models import Psychologist

class Blog(models.Model):
    author = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name="blog_author")
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='blogs/')
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"slug": self.slug})

    class Meta:
        verbose_name_plural = "Блоги"