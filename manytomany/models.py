from django.db import models

# Create your models here.
class ManyActor(models.Model):
    first_name    = models.CharField(max_length=45)
    last_name     = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    jointt=models.ManyToManyField('ManyMovie',through='ManyActor_Movie',related_name='actor')
    class Meta: 
        db_table = "manyactors"
class ManyMovie(models.Model):
    title        = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    class Meta: 
        db_table = "manymovies"
class ManyActor_Movie(models.Model):
    actor = models.ForeignKey('ManyActor', on_delete=models.CASCADE)
    movie = models.ForeignKey('ManyMovie', on_delete=models.CASCADE)
    class Meta: 
        db_table = "manyactors_movies"

# 지금 하려고 하는 것
# ManyActor 정보로 ManyMovie 정보 불러오기