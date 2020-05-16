from django.db import models

# Create your models here.

#ORM (object Relation Mapping)


class Genre(models.Model):
    name = models.CharField(max_length = 255)

    def __str__(self):
        return self.name 




class Movie(models.Model):
    title = models.CharField(max_length = 255)
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.IntegerField()
    image = models.CharField(max_length = 500)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.release_year) + " | " + str(self.title) + " | " + str(self.price)