# Generated by Django 2.2.24 on 2021-11-21 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('nacionalidad', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]