from django.db import models

class Link(models.Model):
    title = models.CharField(max_length=100)
    link = models.CharField(max_length=150)

    def __str__(self):
        return self.title
