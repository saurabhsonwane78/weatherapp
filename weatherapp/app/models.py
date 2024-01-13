from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

class Author(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

