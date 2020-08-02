from premier_league import models
from utils.requests_client import RequestsClient


class PremierLeagueMatchesIngest:

    URL = 'http://api.football-data.org/v2/competitions/PL/matches'

    # TODO - change to environmental variable
    API_KEY = ''

    def start_ingest(self, season_start):
        params = {
            'season': season_start,
        }
        response = RequestsClient().get(self.URL, params, self.API_KEY)
        if not response:
            return False

        season, _ = models.PremierLeagueSeason.objects.get_or_create(
            start_year=season_start,
            end_year=season_start + 1,
        )

        for match in response['matches']:
            home_team, _ = models.PremierLeagueTeam.objects.get_or_create(
                name=match['homeTeam']['name'],
            )
            away_team, _ = models.PremierLeagueTeam.objects.get_or_create(
                name=match['awayTeam']['name'],
            )
            match_query = models.PremierLeagueMatch.objects.filter(
                season=season,
                home_team=home_team,
                away_team=away_team,
            )
            if not match_query:
                models.PremierLeagueMatch.objects.create(
                    season=season,
                    home_team=home_team,
                    away_team=away_team,
                    match_date=match['utcDate'],
                    home_score=match['score']['fullTime']['homeTeam'],
                    away_score=match['score']['fullTime']['awayTeam'],
                )

        return True
