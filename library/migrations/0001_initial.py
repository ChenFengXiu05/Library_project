# Generated by Django 4.2.10 on 2024-03-20 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("gender", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Publisher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=30)),
                ("address", models.CharField(max_length=30)),
                ("city", models.CharField(max_length=12)),
                ("state_province", models.CharField(max_length=30)),
                ("country", models.CharField(max_length=12)),
                ("website", models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("publish_date", models.DateField()),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="library.author"
                    ),
                ),
                (
                    "publishers",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="library.publisher",
                    ),
                ),
            ],
        ),
    ]
