from django.core.management.base import BaseCommand

from nba.ingest import NBAMatchesIngest


class Command(BaseCommand):

    help = 'Imports all NBA matches for a season'

    def add_arguments(self, parser):
        parser.add_argument('season_start', type=int)

    def handle(self, *args, **options):
        season_start = options['season_start']
        season_end = season_start + 1
        self.stdout.write(self.style.SUCCESS(
            f'Importing NBA matches for'
            f' {season_start}/{season_end} season ...'
        ))
        success = NBAMatchesIngest().start_ingest(season_start)
        if not success:
            self.stdout.write(self.style.ERROR(
                'Could not import matches. Please check logs'
            ))
        self.stdout.write(self.style.SUCCESS(
            'Import finished'
        ))
