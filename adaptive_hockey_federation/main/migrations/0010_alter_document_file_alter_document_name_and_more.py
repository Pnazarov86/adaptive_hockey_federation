# Generated by Django 4.2.8 on 2024-01-29 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0009_remove_player_document_document_player_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="document",
            name="file",
            field=models.FileField(max_length=256, unique=True, upload_to="documents"),
        ),
        migrations.AlterField(
            model_name="document",
            name="name",
            field=models.CharField(
                help_text="Наименование", max_length=256, verbose_name="Наименование"
            ),
        ),
        migrations.AddConstraint(
            model_name="document",
            constraint=models.UniqueConstraint(
                fields=("file", "player"), name="player_docume_unique"
            ),
        ),
    ]
