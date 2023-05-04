from django.db import models


class SettingsHomePage(models.Model):
    title_site = models.CharField(max_length=256)

    # logo = models.ImageField(upload_to='settings/logo/')
    banner_one = models.ImageField(upload_to='settings/banner/')
    banner_one_title = models.CharField(max_length=256)
    banner_one_desc = models.TextField()
    banner_two = models.ImageField(upload_to='settings/banner/')
    banner_two_title = models.CharField(max_length=256)
    banner_two_desc = models.TextField()

    def __str__(self):
        return self.title_site