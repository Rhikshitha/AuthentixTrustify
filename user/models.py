from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import timedelta,datetime

class Account(AbstractUser):
    email = models.CharField(max_length=50,unique=True)
    token = models.CharField(max_length=50,default="")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def save(self,*args,**kwargs):
        if self._state.adding and not self.is_superuser:
            self.is_active=False
        super().save(*args,**kwargs)
            

    def __str__(self):
        return self.username
