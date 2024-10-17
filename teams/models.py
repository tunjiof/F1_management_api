from django.db import models
from users.models import User

# Create your models here.

class TeamModel(models.Model):
    # user = models.OneToOneField(User,on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=True)
    base = models.CharField(max_length=200, blank=True)
    team_principal = models.CharField(max_length=200, blank=True)
    championship_won = models.IntegerField(default=0, blank=True)
