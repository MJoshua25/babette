# Generated by Django 2.2.8 on 2020-05-27 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_commentaire_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentaire',
            name='article',
        ),
    ]
