# Generated by Django 2.2.8 on 2020-05-28 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteConfig', '0005_auto_20200528_1157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('logo_1', models.ImageField(upload_to='siteConfig')),
                ('status', models.BooleanField(default=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsors',
            },
        ),
    ]
