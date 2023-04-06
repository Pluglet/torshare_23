import uuid
from django.db import models

# Create your models here.

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/", default="images/default.png")
    tags = models.ManyToManyField('Tag', blank=True)
    curator = models.ForeignKey('users.Profile', on_delete=models.CASCADE, related_name='curator')
    url = models.URLField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name