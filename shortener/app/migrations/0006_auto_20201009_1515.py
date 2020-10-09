# Generated by Django 3.1.2 on 2020-10-09 15:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201009_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='report',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
