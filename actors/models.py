from django.db import models
# from movies.models import Movie
# Create your models here.
class Actor(models.Model):
    name = models.CharField(max_length=80)
    bio = models.TextField()
    photo = models.ImageField(upload_to ='uploads/', height_field=30, width_field=15)
    # filmography = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name