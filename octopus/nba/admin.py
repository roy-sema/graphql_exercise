from django.contrib import admin

from nba import models


class NBASeasonAdmin(admin.ModelAdmin):
    ordering = (
        'start_year',
    )
    search_fields = (
        'start_year',
        'start_end',
    )


class NBATeamAdmin(admin.ModelAdmin):
    ordering = (
        'name',
    )
    search_fields = (
        'name',
    )


class NBAMatchAdmin(admin.ModelAdmin):
    ordering = (
        'match_date',
    )
    search_fields = (
        'home_team__name',
        'away_team__name',
    )


admin.site.register(models.NBASeason, NBASeasonAdmin)
admin.site.register(models.NBATeam, NBATeamAdmin)
admin.site.register(models.NBAMatch, NBAMatchAdmin)
