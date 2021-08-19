# Generated by Django 3.1.7 on 2021-08-14 02:23

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('namelist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devilname',
            options={'ordering': ['name'], 'verbose_name': 'Nome'},
        ),
        migrations.AlterModelManagers(
            name='devilname',
            managers=[
                ('randoms', django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name='devilname',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Data de criação do nome do capeta', verbose_name='Data de criação'),
        ),
    ]