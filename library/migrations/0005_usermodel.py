# Generated by Django 4.2.10 on 2024-03-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0004_remove_book_publishers_book_publishers"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserModel",
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
                ("username", models.CharField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=100)),
                ("age", models.IntegerField(default=18)),
            ],
        ),
    ]