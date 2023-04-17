# Generated by Django 4.2 on 2023-04-17 08:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MainSpecialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PsychologistStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Psychologist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, null=True)),
                ('surname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=50)),
                ('sex', models.CharField(choices=[('М', 'Мужской'), ('Ж', 'Женский')], max_length=7)),
                ('brief_description_work', models.CharField(max_length=500)),
                ('bio', models.TextField()),
                ('education', models.TextField()),
                ('online_consultation', models.CharField(choices=[('Д', 'Да'), ('Н', 'Нет')], max_length=3)),
                ('cost_of_online_consultation', models.IntegerField(blank=True, help_text='руб', null=True)),
                ('personal_reception', models.CharField(choices=[('Д', 'Да'), ('Н', 'Нет')], max_length=3)),
                ('cost_of_personal_reception', models.IntegerField(blank=True, help_text='руб', null=True)),
                ('address_of_the_reception_room', models.CharField(blank=True, max_length=500, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('skype', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('additional_specialization_one', models.ForeignKey(blank=True, default='None', null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='psychologist.additionalspecialization')),
                ('main_specialization', models.ForeignKey(default='None', on_delete=django.db.models.deletion.SET_DEFAULT, to='psychologist.mainspecialization')),
                ('status', models.ForeignKey(default='None', on_delete=django.db.models.deletion.SET_DEFAULT, to='psychologist.psychologiststatus')),
            ],
        ),
    ]
