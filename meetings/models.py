from django.db import models

class Meeting(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    descripcion = models.TextField(max_length=1000, null=True)

class About(models.Model):
    text = models.TextField(max_length=2000, null=True)