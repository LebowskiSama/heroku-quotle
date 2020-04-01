from django.db import models
from datetime import date, datetime

class fur(models.Model):
    
    title = models.TextField()
    quotes = models.TextField()

    def __str__(self):

        return self.title