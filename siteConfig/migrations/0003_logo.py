# Generated by Django 3.0.6 on 2020-05-28 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteConfig', '0002_footer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='siteConfig')),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Logos',
            },
        ),
    ]
