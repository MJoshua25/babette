# Generated by Django 3.0.6 on 2020-05-28 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_commentaire_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='article',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='commentaires', to='blog.Article'),
            preserve_default=False,
        ),
    ]
