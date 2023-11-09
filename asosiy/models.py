from django.db import models

class Reja(models.Model):
    name = models.CharField(max_length=30)
    task = models.TextField()
    date = models.DateField()
    progres = models.CharField(max_length=50)

    def __str__(self):
        return self.name
