# Generated by Django 4.0.6 on 2022-08-25 22:08

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entrada', '0001_initial'),
        ('favoritos', '0004_alter_favorites_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='favorites',
            unique_together={('user', 'entry')},
        ),
    ]
