from django.db import models
# from django.contrib.auth.models import User
# from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=50)
    # director = models.ForeignKey(Actor, on_delete=models.CASCADE)
    description = models.TextField()
    date_released = models.CharField(max_length=20)
    instructions = models.TextField()
    photo = models.ImageField(upload_to ='uploads/', height_field=30, width_field=15)
    # actors = models.ForeignKey(Actor, on_delete=models.CASCADE)
    genre = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.actors}"

