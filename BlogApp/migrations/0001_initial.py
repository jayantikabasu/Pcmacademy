# Generated by Django 5.0.1 on 2024-02-11 16:30

import BlogApp.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage_Head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bg_img', models.ImageField(help_text='About head bg | width= 848.8px height= 600px ', upload_to='aboutpagehead', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), BlogApp.models.Head_About_diamension])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nav1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(help_text='NITD Logo | width= 250px height= 80px ', upload_to='Nav_logo', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png']), BlogApp.models.NITD_Logo_diamension])),
                ('email', models.EmailField(help_text='Enter Email of Company | max_length = 120', max_length=120)),
                ('call_number', models.CharField(help_text='Enter phone_number of Company', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
