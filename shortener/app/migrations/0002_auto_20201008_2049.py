# Generated by Django 3.1.2 on 2020-10-08 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short',
            field=models.URLField(unique=True),
        ),
    ]