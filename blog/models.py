from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
