# Generated by Django 4.2.8 on 2024-02-10 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_setting_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="role",
            field=models.CharField(
                choices=[
                    ("Представитель команды", "Представитель команды"),
                    ("Модератор", "Модератор"),
                    ("Администратор", "Администратор"),
                    ("admin", "Суперпользователь"),
                ],
                default="Представитель команды",
                help_text="Уровень прав доступа",
                max_length=21,
                verbose_name="Роль",
            ),
        ),
    ]
