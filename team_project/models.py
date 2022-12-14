from django.contrib.auth.models import User
from django.db import models

# Create your models here.
#from user.models import User


class Team(models.Model):
    team_name = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.team_name}'


class Project(models.Model):
    team = models.OneToOneField(Team, on_delete=models.CASCADE) #팀 모델과 일대일 관계
    title = models.CharField(max_length=30)
    date_start = models.DateField()
    date_end = models.DateField()
    introduce = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'./{self.pk}/'

class Participant(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'[{self.pk}] [{self.team.team_name}] {self.user.username}'
