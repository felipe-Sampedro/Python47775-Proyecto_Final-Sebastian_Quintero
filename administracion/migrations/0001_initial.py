# Generated by Django 4.2.7 on 2023-11-21 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('representante_legal', models.CharField(max_length=50)),
                ('razon_social', models.CharField(max_length=80)),
                ('doc_nit', models.IntegerField()),
                ('descripcion', models.CharField(max_length=250)),
                ('num_inmuebles', models.IntegerField()),
                ('tipo_bien_raiz', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
                ('fecha_actualizacion', models.DateField()),
            ],
        ),
    ]