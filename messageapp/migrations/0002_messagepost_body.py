# Generated by Django 3.1.3 on 2020-11-13 18:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messageapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagepost',
            name='body',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]