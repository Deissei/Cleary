# Generated by Django 4.2 on 2023-04-24 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('psychologist', '0010_alter_psychologist_online_consultation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychologist',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
    ]
