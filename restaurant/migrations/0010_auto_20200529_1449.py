# Generated by Django 2.2.8 on 2020-05-29 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0009_auto_20200529_0831'),
    ]

    operations = [
        migrations.AddField(
            model_name='tel',
            name='call',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tel',
            name='dispo',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
