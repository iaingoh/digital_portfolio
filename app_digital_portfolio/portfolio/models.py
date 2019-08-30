from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# TODO: create Project model

class Project(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(default='default.jpg')

    def __str__(self):
        return self.title

class ProjectSubtitle(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    # List of bullet points
    
    # def __str__(self):
    #     return self.title
