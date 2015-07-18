from django.db import models
from tinymce.models import HTMLField

class ImageModel(models.Model):
    img = models.ImageField(upload_to='riders')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blogs')
    date = models.DateField(auto_now_add = True)
    intro = HTMLField()
    content = HTMLField()
    url = models.CharField(max_length=100, null=True)
    images = models.ManyToManyField(ImageModel, null=True, blank=True)

    def __str__(self):
        return self.title