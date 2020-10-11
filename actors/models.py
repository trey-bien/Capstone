from django.db import models
# from movies.models import Movie


class Actor(models.Model):
    name = models.TextField(max_length=80)
    bio = models.CharField(max_length=1000)
    photo = models.ImageField(upload_to='images/', null=True, blank=True)
    # filmography = models.ForeignKey(Movie, on_delete=models.CASCADE, default=True)

    def __str__(self):
        return self.name