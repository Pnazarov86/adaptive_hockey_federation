# Generated by Django 4.2.9 on 2024-04-16 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_setting_disciplines'),
        ('competitions', '0003_remove_competition_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='disciplines',
            field=models.ManyToManyField(help_text='Дисциплины', related_name='competitions', to='main.disciplinename', verbose_name='Дисциплины'),
        ),
    ]