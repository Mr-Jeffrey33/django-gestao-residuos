# Generated by Django 4.2 on 2023-04-27 13:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("entrada", "0002_alter_entrada_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="entrada",
            options={"ordering": ["-id_entrada"]},
        ),
    ]