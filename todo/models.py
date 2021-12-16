from django.db import models
from users.models import User


class Project(models.Model):
    name = models.CharField(unique=True, max_length=64)
    repository_link = models.URLField(blank=True, null=True)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name}'


class ToDo(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f'Project {self.project}: {self.text},user: {self.user}, is active: {self.is_active}'
