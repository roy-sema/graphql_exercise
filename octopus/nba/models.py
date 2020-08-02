from django.db import models

from core.models import BaseSeason, BaseTeam, BaseMatch


class NBASeason(BaseSeason):
    pass


class NBATeam(BaseTeam):
    pass


class NBAMatch(BaseMatch):
    season = models.ForeignKey(
        NBASeason,
        on_delete=models.CASCADE,
        related_name='matches',
    )
    home_team = models.ForeignKey(
        NBATeam,
        on_delete=models.CASCADE,
        related_name='home_matches',
    )
    away_team = models.ForeignKey(
        NBATeam,
        on_delete=models.CASCADE,
        related_name='away_matches',
    )

    def __str__(self):
        return f'{self.home_team.name} : {self.home_score} ' \
               f'- {self.away_team.name} : {self.away_score}'
