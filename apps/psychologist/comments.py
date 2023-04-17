from django.db import models
from apps.psychologist.models import Psychologist


class Comment(models.Model):
    to_whom = models.ForeignKey(Psychologist, on_delete=models.CASCADE, related_name='comment_psylo')
    name = models.CharField(max_length=30)
    message = models.TextField()
    created_at = models.DateField()

    def __str__(self):
        return f"{self.name} -> {self.to_whom}" 


    class Meta:
        verbose_name_plural = "Коментарии"