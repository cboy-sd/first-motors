# Generated by Django 2.1.15 on 2022-05-07 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0013_team_first_odj'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='first_odj',
            new_name='firstm_member',
        ),
    ]
