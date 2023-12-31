# Generated by Django 5.0 on 2023-12-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="students",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("full_name", models.CharField(max_length=250, verbose_name="ФИО")),
                ("email", models.EmailField(max_length=254, verbose_name="Почта")),
                (
                    "phone_number",
                    models.CharField(max_length=18, verbose_name="Номер телефона"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("Рассмотрение", "Рассмотрение"),
                            ("Отклонено", "Отклонено"),
                            ("Принято", "Принято"),
                        ],
                        max_length=255,
                        verbose_name="Статус",
                    ),
                ),
            ],
        ),
    ]
