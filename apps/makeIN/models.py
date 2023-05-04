from django.db import models

class MakeAnAppointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=256)
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} -> {self.subject}"