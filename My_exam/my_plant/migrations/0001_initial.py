# Generated by Django 4.1.4 on 2022-12-21 07:42

import My_exam.my_plant.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Outdoor Plants', 'Outdoor Plants'), ('Indoor Plants', 'Indoor Plants')], max_length=14)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2, 'It should consist minimum of 2 characters'), My_exam.my_plant.models.only_letter])),
                ('image', models.URLField()),
                ('description', models.TextField()),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2, 'It should consist of a minimum of 2 characters')])),
                ('first_name', models.CharField(max_length=20, validators=[My_exam.my_plant.models.name_validate])),
                ('last_name', models.CharField(max_length=20, validators=[My_exam.my_plant.models.name_validate])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
