# Generated by Django 4.2.7 on 2023-11-29 07:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("review", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ticket",
            name="description",
            field=models.TextField(
                blank=True, max_length=2048, verbose_name="Description"
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="", verbose_name="Image"
            ),
        ),
        migrations.AlterField(
            model_name="ticket",
            name="title",
            field=models.CharField(max_length=128, verbose_name="Titre"),
        ),
    ]
