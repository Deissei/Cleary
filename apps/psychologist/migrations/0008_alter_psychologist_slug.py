# Generated by Django 4.2 on 2023-04-18 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologist', '0007_alter_comment_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psychologist',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]