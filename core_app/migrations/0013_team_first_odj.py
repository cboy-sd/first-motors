# Generated by Django 2.1.15 on 2022-05-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0012_team_is_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='first_odj',
            field=models.BooleanField(default=False),
        ),
    ]
