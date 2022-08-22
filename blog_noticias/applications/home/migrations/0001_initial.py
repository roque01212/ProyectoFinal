<<<<<<< HEAD
# Generated by Django 4.0.6 on 2022-08-21 15:51
=======
# Generated by Django 4.0.6 on 2022-08-19 18:00
>>>>>>> Camilo

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30, verbose_name='Nombre completo')),
                ('last_name', models.CharField(max_length=30, verbose_name='Apellido')),
                ('image', models.ImageField(upload_to='About', verbose_name='Foto')),
                ('date_birth', models.DateField(blank=True, null=True, verbose_name='fecha Nacimiento')),
                ('age', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20, verbose_name='Telefono')),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Informacion Personal',
                'verbose_name_plural': 'Sobre Nosotros',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('email', models.EmailField(max_length=254)),
                ('messagge', models.TextField()),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='Suscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscriptores',
            },
        ),
    ]
