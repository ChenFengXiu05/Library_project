# Generated by Django 4.2.10 on 2024-03-20 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("library", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="book",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="library.author",
                verbose_name="作者",
            ),
        ),
        migrations.AlterField(
            model_name="book",
            name="publish_date",
            field=models.DateField(verbose_name="出版时间"),
        ),
        migrations.AlterField(
            model_name="book",
            name="publishers",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="library.publisher",
                verbose_name="出版社",
            ),
        ),
    ]
