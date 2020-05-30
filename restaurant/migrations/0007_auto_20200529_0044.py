# Generated by Django 2.2.8 on 2020-05-29 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_guest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Titreguest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255, unique=True)),
                ('soustitre', models.CharField(max_length=255, unique=True)),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Titreguest',
                'verbose_name_plural': 'Titreguests',
            },
        ),
        migrations.RemoveField(
            model_name='guest',
            name='titre',
        ),
    ]