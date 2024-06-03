# Generated by Django 4.2.10 on 2024-03-18 10:22

import phonenumber_field.modelfields
import phonenumber_field.validators
from django.db import migrations

import users.validators


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_alter_user_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                blank=True,
                help_text="Номер телефона, допустимый формат - +7 ХХХ ХХХ ХХ ХХ",
                max_length=128,
                region=None,
                validators=[
                    phonenumber_field.validators.validate_international_phonenumber,
                    users.validators.zone_code_without_seven_hundred,
                ],
                verbose_name="Актуальный номер телефона",
            ),
        ),
    ]
