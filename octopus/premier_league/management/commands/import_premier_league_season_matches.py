from django.core.management.base import BaseCommand

from premier_league.ingest import PremierLeagueMatchesIngest


class Command(BaseCommand):

    help = 'Imports all premier league matches for a season'

    def add_arguments(self, parser):
        parser.add_argument('season_start', type=int)

    def handle(self, *args, **options):
        season_start = options['season_start']
        season_end = season_start + 1
        self.stdout.write(self.style.SUCCESS(
            f'Importing premier league matches for'
            f' {season_start}/{season_end} season ...'
        ))
        success = PremierLeagueMatchesIngest().start_ingest(season_start)
        if not success:
            self.stdout.write(self.style.ERROR(
                'Could not import matches. Please check logs'
            ))
        self.stdout.write(self.style.SUCCESS(
            'Import finished'
        ))
