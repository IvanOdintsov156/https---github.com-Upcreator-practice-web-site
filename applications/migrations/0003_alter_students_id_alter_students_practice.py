# Generated by Django 5.0 on 2023-12-27 18:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("applications", "0002_initial"),
        ("moderators", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="students",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="students",
            name="practice",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="moderators.trainingdirections",
                verbose_name="Направление практики",
            ),
        ),
    ]
