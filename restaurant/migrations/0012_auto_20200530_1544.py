# Generated by Django 3.0.6 on 2020-05-30 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0011_event_ticket'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Ticket',
        ),
    ]
