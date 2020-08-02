from django.contrib import admin

from premier_league import models


class PremierLeagueSeasonAdmin(admin.ModelAdmin):
    ordering = (
        'start_year',
    )
    search_fields = (
        'start_year',
        'start_end',
    )


class PremierLeagueTeamAdmin(admin.ModelAdmin):
    ordering = (
        'name',
    )
    search_fields = (
        'name',
    )


class PremierLeagueMatchAdmin(admin.ModelAdmin):
    ordering = (
        'match_date',
    )
    search_fields = (
        'home_team__name',
        'away_team__name',
    )


admin.site.register(models.PremierLeagueSeason, PremierLeagueSeasonAdmin)
admin.site.register(models.PremierLeagueTeam, PremierLeagueTeamAdmin)
admin.site.register(models.PremierLeagueMatch, PremierLeagueMatchAdmin)
