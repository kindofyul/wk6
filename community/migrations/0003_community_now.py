# Generated by Django 4.2.1 on 2023-05-11 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_remove_community_now'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='now',
            field=models.BooleanField(default=False),
        ),
    ]
