# Generated by Django 2.0.4 on 2018-05-17 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_estadotarea'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='fechaTermino',
            field=models.DateField(blank=True, null=True, verbose_name='%d-%m-%Y'),
        ),
    ]
