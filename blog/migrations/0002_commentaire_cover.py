# Generated by Django 2.2.8 on 2020-05-27 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='cover',
            field=models.ImageField(default='', upload_to='singleblog'),
            preserve_default=False,
        ),
    ]