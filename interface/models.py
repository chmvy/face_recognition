from django.db import models

# Create your models here.

class PersonInfo(models.Model):
    resultCode = models.IntegerField()
    CustomerName = models.TextField()
    personId = models.TextField()
    CardNO = models.CharField(max_length=200)
    CustomerIDNO = models.CharField(max_length=200)
    Photo = models.URLField()