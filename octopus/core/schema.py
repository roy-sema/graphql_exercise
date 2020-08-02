import graphene

# import premier_league.schema
from premier_league import schema as premier_league_schema
from nba import schema as nba_schema


class Query(premier_league_schema.Query, nba_schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query)
