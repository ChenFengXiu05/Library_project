# Generated by Django 4.2.10 on 2024-03-20 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0003_alter_author_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="publishers",
        ),
        migrations.AddField(
            model_name="book",
            name="publishers",
            field=models.ManyToManyField(to="library.publisher", verbose_name="出版社"),
        ),
    ]
