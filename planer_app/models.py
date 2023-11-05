from django.db import models

# Create your models here.

class PlanerQuest(models.Model):
    quest_id = models.AutoField(db_column='ID', primary_key=True)
    user_id = models.IntegerField(db_column='User_ID')
    type = models.CharField(db_column='Type', max_length=20)
    title = models.CharField(db_column='Title', max_length=200)
    description = models.CharField(db_column='Description', max_length=500)
    done = models.BooleanField(db_column='Done', default=False)
