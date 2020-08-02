from datetime import datetime


def parse_date(date_string):
    """
    date_string needs to be in this format or will return None
    """
    try:
        return datetime.strptime(date_string, '%Y-%m-%d')
    except (ValueError, TypeError):
        return None
