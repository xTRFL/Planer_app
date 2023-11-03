from django.db import models

# Create your models here.

class PlanerQuest(models.Model):
    movie_id = models.AutoField(db_column='ID', primary_key=True)
    type = models.CharField(db_column='Type', max_length=20)
    title = models.CharField(db_column='Title', max_length=200)
    description = models.CharField(db_column='Description', max_length=500)

    class Meta:
        managed = True
        db_table = 'movie_titles_final'