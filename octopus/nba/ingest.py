from nba import models
from utils.requests_client import RequestsClient


class NBAMatchesIngest:

    requests_client = RequestsClient()

    URL = 'https://www.balldontlie.io/api/v1/games'
    PER_PAGE = 100

    def start_ingest(self, season_start):
        season, _ = models.NBASeason.objects.get_or_create(
            start_year=season_start,
            end_year=season_start + 1,
        )

        params = {
            'seasons[]': season_start,
            'per_page': self.PER_PAGE,
        }
        response = self.requests_client.get(self.URL, params)
        if not response:
            return False

        return self.create_matches(response, season)

    def create_matches(self, response, season):
        for match in response['data']:
            home_team, _ = models.NBATeam.objects.get_or_create(
                name=match['home_team']['full_name'],
            )
            away_team, _ = models.NBATeam.objects.get_or_create(
                name=match['visitor_team']['full_name'],
            )
            match_query = models.NBAMatch.objects.filter(
                season=season,
                home_team=home_team,
                away_team=away_team,
            )
            if not match_query:
                models.NBAMatch.objects.create(
                    season=season,
                    home_team=home_team,
                    away_team=away_team,
                    match_date=match['date'],
                    home_score=match['home_team_score'],
                    away_score=match['visitor_team_score'],
                )

        next_page = response['meta']['next_page']
        if next_page:
            params = {
                'seasons[]': season.start_year,
                'per_page': self.PER_PAGE,
                'page': next_page,
            }
            response = self.requests_client.get(self.URL, params)
            if not response:
                return False
            return self.create_matches(response, season)

        return True
