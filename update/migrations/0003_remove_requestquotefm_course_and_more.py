# Generated by Django 5.0.1 on 2024-04-13 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('update', '0002_requestquotefm'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestquotefm',
            name='course',
        ),
        migrations.AddField(
            model_name='requestquotefm',
            name='qualification',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
