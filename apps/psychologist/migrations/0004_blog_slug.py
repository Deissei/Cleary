# Generated by Django 4.2 on 2023-04-17 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologist', '0003_psychologist_image_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
    ]
