# Generated by Django 2.0.4 on 2018-05-17 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_tarea_fechatermino'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoTarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='estadotarea',
            old_name='ETarea',
            new_name='Estado',
        ),
    ]