from graphene_django import DjangoObjectType
import graphene

from premier_league import models
from utils.pagination import Pagination
from utils.filter_match_by_date import filter_match_by_date


class PremierLeagueSeasonType(DjangoObjectType):
    class Meta:
        model = models.PremierLeagueSeason


class PremierLeagueTeamType(DjangoObjectType):
    class Meta:
        model = models.PremierLeagueTeam


class PremierLeagueMatchType(DjangoObjectType):
    class Meta:
        model = models.PremierLeagueMatch


class Query(graphene.ObjectType):
    premier_league_matches = graphene.List(
        PremierLeagueMatchType,
        date=graphene.String(),
        page=graphene.Int(),
        per_page=graphene.Int(),
    )

    def resolve_premier_league_matches(
            self, info, date=None, page=None, per_page=None):
        query = models.PremierLeagueMatch.objects.order_by('match_date')
        if date:
            query = filter_match_by_date(query, date)
        return Pagination().get_paginated_results(query, page, per_page)


schema = graphene.Schema(query=Query)
