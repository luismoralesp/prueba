# Generated by Django 2.2.3 on 2019-07-11 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='region',
            name='monicipios',
        ),
        migrations.AddField(
            model_name='region',
            name='municipios',
            field=models.ManyToManyField(to='app.Municipio'),
        ),
    ]