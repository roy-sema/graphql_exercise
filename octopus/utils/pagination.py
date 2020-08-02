import math


class Pagination:
    PER_PAGE = 40

    def get_paginated_results(self, query, page=None, per_page=None):
        if not page:
            page = 1
        if not per_page:
            per_page = self.PER_PAGE

        total_pages = math.ceil(query.count() / per_page)

        if page > total_pages:
            return []

        start = (per_page * page) - per_page
        end = start + per_page
        return query[start:end]
