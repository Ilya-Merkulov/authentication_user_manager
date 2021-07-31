from django.db import models

# Create your models here.
class Groups(models.Model):
    GroupName = models.CharField(max_length=100, unique=True)
    GroupDescription = models.TextField(max_length=600)