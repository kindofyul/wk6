# Generated by Django 4.2.1 on 2023-05-11 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='now',
        ),
    ]
