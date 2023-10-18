from django.db import models

# Create your models here.


class Libray(models.Model):
    title = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.title
