from django.db import models


# Create your models here.

class Person(models.Model):  # все модели джанго наследуются от models.Model
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    age = models.IntegerField()
    city = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to='photos')



    def __str__(self):
        return self.name

