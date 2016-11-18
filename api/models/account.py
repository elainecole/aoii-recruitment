from django.contrib.auth.models import User
from django.db import models


class Account(models.Model):
    '''
    Holds meta information about an Account, not used to login.
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=63, unique=True, blank=False)
