# Generated by Django 4.1.1 on 2022-11-17 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("el_lector", "0002_alter_domicilio_piso")]

    operations = [
        migrations.AlterField(
            model_name="imprenta",
            name="email",
            field=models.EmailField(max_length=20, verbose_name="email"),
        )
    ]