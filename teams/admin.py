from django.contrib import admin

# Register your models here.
from .models import TeamModel

class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'base', 'team_principal', 'championship_won')
    search_fields = ('name', 'base')

admin.site.register(TeamModel, TeamAdmin)
