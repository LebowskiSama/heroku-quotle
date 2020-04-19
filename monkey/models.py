from django.db import models
from datetime import date, datetime

class fur(models.Model):

    imdbID = models.TextField(unique=True, null=False)
    quotes = models.TextField()

    def __str__(self):

        return self.imdbID