# Generated by Django 2.2.3 on 2019-07-11 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=255)),
                ('estado', models.IntegerField(choices=[('Activo', 0), ('Inactivo', 0)])),
            ],
            options={
                'verbose_name': 'Municipio',
                'verbose_name_plural': 'Municipios',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField(unique=True, verbose_name='Código')),
                ('nombre', models.CharField(max_length=255)),
                ('monicipios', models.ManyToManyField(to='app.Municipio')),
            ],
            options={
                'verbose_name': 'Región',
                'verbose_name_plural': 'Regiones',
            },
        ),
    ]
