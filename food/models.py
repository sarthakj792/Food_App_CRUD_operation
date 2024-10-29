from django.db import models

# Create your models here.
class Dishlist(models.Model):

    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    propic = models.ImageField(upload_to='images/')



class User(models.Model):

    def __str__(self):
        return self.username
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
