# Generated by Django 5.0.1 on 2024-02-14 17:27

import BlogApp.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0007_blogpage_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage_blog',
            name='author_image',
            field=models.ImageField(help_text=' Author image | width = 800px height = 850px ', null=True, upload_to='author_image', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg']), BlogApp.models.Author_img_diamension]),
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=70)),
                ('phone', models.IntegerField(blank=True, null=True)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('relation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='BlogApp.blogpage_blog')),
            ],
        ),
    ]