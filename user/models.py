from django.db import models
from django.contrib.auth.models import AbstractUser
from group.models import Groups


class User(AbstractUser):   
    #id
    group_id = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True, blank=True) 
   
    