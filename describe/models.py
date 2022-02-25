from django.contrib.auth.models import User
from django.db import models


class Journal(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    insult = models.CharField(max_length=50)
    user_to = models.SmallIntegerField()
