from django.db import models

class ImageModel(models.Model):
    img = models.ImageField(upload_to='riders')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Rider(models.Model):
    bio = models.TextField(blank=True)
    birth = models.DateField()
    facebook = models.URLField(blank=True)
    image = models.ImageField(upload_to='riders')
    images = models.ManyToManyField(ImageModel, blank=True)
    instagram = models.URLField(blank=True)
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    ride = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100, blank=True)
    twitter = models.URLField(blank=True)
    url = models.CharField(max_length=100)
    web = models.URLField(blank=True)


    def __str__(self):
        return self.name