from django.db import models


class Priority(models.Model):
    priority = models.CharField(max_length=15, unique=True)


class Group(models.Model):
    name = models.CharField(
        "Name of a group", max_length=15)


class Task(models.Model):
    name = models.CharField(
        "Name of a task", max_length=15, blank=True, null=True)
    description = models.CharField(
        "Description of a task", max_length=50, blank=True, null=True)
    group = models.ForeignKey(
        Group, related_name='tasks', blank=True, null=True, on_delete=models.CASCADE)
    priority = models.ForeignKey(
        Priority, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.id} : {self.name}'
