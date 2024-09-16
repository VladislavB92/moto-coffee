from django.db import models

class Coffee(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    roast_level = models.IntegerField(default=0)
    acidity = models.IntegerField(default=0)
    country_of_origin = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Biker(models.Model):
    model = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

