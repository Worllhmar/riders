from django.db import models

class ImageModel(models.Model):
    img = models.ImageField(upload_to='events')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    dateTime = models.DateField()
    description = models.TextField(blank="True")
    image = models.ImageField(upload_to='events')
    images = models.ManyToManyField(ImageModel, blank=True)
    mapa = models.TextField(blank=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ticketlink = models.CharField(max_length=100, blank=True)
    url = models.CharField(max_length=100)

    def __str__(self):
        return self.name
