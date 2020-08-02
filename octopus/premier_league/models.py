from django.db import models

from core.models import BaseSeason, BaseTeam, BaseMatch


class PremierLeagueSeason(BaseSeason):
    pass


class PremierLeagueTeam(BaseTeam):
    pass


class PremierLeagueMatch(BaseMatch):
    season = models.ForeignKey(
        PremierLeagueSeason,
        on_delete=models.CASCADE,
        related_name='matches',
    )
    home_team = models.ForeignKey(
        PremierLeagueTeam,
        on_delete=models.CASCADE,
        related_name='home_matches',
    )
    away_team = models.ForeignKey(
        PremierLeagueTeam,
        on_delete=models.CASCADE,
        related_name='away_matches',
    )

    def __str__(self):
        return f'{self.home_team.name} : {self.home_score} ' \
               f'- {self.away_team.name} : {self.away_score}'
