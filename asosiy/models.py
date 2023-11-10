from django.db import models
from django.contrib.auth.models import *

class Reja(models.Model):
    t_name = models.CharField(max_length=30)
    t_detail = models.TextField()
    date = models.DateField()
    progress = models.CharField(max_length=50)
    egasi = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.t_name
