# Generated by Django 2.0.4 on 2018-05-17 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_tarea_fechainicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='fechaInicio',
            field=models.DateField(verbose_name='%d-%m-%Y'),
        ),
    ]
