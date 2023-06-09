# Generated by Django 4.2 on 2023-04-17 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('psychologist', '0002_alter_additionalspecialization_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='psychologist',
            name='image',
            field=models.ImageField(default=1, upload_to='psychologist'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='blogs/')),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_author', to='psychologist.psychologist')),
            ],
            options={
                'verbose_name_plural': 'Блоги',
            },
        ),
    ]
