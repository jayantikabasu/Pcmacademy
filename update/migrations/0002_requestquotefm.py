# Generated by Django 5.0.1 on 2024-02-12 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestQuoteFm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email_id', models.CharField(max_length=100)),
                ('course', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]