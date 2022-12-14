# Generated by Django 3.0.14 on 2022-11-25 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrenadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('lancha', models.IntegerField()),
                ('club', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Timoneles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre_barco', models.CharField(max_length=50)),
                ('numero_vela', models.IntegerField()),
                ('club', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Tripulantes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('nombre_barco', models.CharField(max_length=50)),
                ('numero_vela', models.IntegerField()),
                ('club', models.CharField(max_length=5)),
                ('peso', models.FloatField()),
            ],
        ),
    ]
