# Generated by Django 4.1.6 on 2023-11-05 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planer_app', '0002_rename_movie_id_planerquest_quest_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='planerquest',
            name='done',
            field=models.BooleanField(db_column='Done', default=False),
        ),
    ]
