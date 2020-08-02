from datetime import timedelta

from utils.parse_date import parse_date


def filter_match_by_date(query, start_date_string):
    start_date = parse_date(start_date_string)
    last_day = start_date + timedelta(days=1)
    return query.filter(match_date__gte=start_date, match_date__lt=last_day)
