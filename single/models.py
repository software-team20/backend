from datetime import datetime

from django.db import models
from django.contrib.auth.models import User



# Create your models here.
import team_project
from team_project.models import Team


class Schedule(models.Model) :
    STATUS = (
        ('개인', 'single'),
        ('팀', 'team')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    how = models.CharField(max_length=10, choices=STATUS, null=True)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    date = models.DateField(null=True)
    startTime = models.TimeField(null=True)
    dueTime = models.TimeField(null=True)
    title = models.CharField(max_length=50, default="")

    def __str__(self):
        return f'[{self.pk}] {self.title}'