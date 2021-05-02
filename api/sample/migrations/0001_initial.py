# Generated by Django 3.2 on 2021-05-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SampleModel",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "sample_attr1",
                    models.CharField(blank=True, max_length=16, null=True),
                ),
                (
                    "sample_attr2",
                    models.PositiveSmallIntegerField(blank=True, null=True),
                ),
            ],
            options={
                "verbose_name": "Sample Datum",
                "verbose_name_plural": "Sample Data",
            },
        ),
    ]