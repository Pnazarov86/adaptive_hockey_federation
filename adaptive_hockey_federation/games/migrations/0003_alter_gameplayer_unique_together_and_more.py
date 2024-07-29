# Generated by Django 4.2.13 on 2024-07-28 10:32

import core.constants
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_gamedataplayer'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='gameplayer',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='gameplayer',
            name='patronymic',
            field=models.CharField(blank=True, max_length=core.constants.UserConstans['NAME_MAX_LENGTH'], verbose_name='Отчество игрока'),
        ),
        migrations.AddConstraint(
            model_name='gameplayer',
            constraint=models.UniqueConstraint(fields=('name', 'last_name', 'patronymic', 'number', 'game_team'), name='player_number_must_be_unique'),
        ),
    ]
