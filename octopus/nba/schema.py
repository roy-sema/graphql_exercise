from graphene_django import DjangoObjectType
import graphene

from nba import models
from utils.filter_match_by_date import filter_match_by_date
from utils.pagination import Pagination


class NBASeasonType(DjangoObjectType):
    class Meta:
        model = models.NBASeason


class NBATeamType(DjangoObjectType):
    class Meta:
        model = models.NBATeam


class NBAMatchType(DjangoObjectType):
    class Meta:
        model = models.NBAMatch


class Query(graphene.ObjectType):
    nba_matches = graphene.List(
        NBAMatchType,
        date=graphene.String(),
        page=graphene.Int(),
        per_page=graphene.Int(),
    )

    def resolve_nba_matches(
            self, info, date=None, page=None, per_page=None):
        query = models.NBAMatch.objects.order_by('match_date')
        if date:
            query = filter_match_by_date(query, date)
        return Pagination().get_paginated_results(query, page, per_page)


schema = graphene.Schema(query=Query)
