# Generated by Django 2.0.4 on 2018-05-20 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_tarea_estadotarea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='estadoTarea',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.EstadoTarea'),
            preserve_default=False,
        ),
    ]