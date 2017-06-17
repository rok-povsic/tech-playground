import graphene
from graphene import resolve_only_args

from data.starwars.models import Character, Episode, Human, Droid, get_droid, get_hero, get_human


class Query(graphene.ObjectType):
    hero = graphene.Field(Character,
                          episode=Episode()
                          )
    human = graphene.Field(Human,
                           id=graphene.String()
                           )
    droid = graphene.Field(Droid,
                           id=graphene.String()
                           )

    @resolve_only_args
    def resolve_hero(self, episode=None):
        return get_hero(episode)

    @resolve_only_args
    def resolve_human(self, id):
        return get_human(id)

    @resolve_only_args
    def resolve_droid(self, id):
        return get_droid(id)


starwars_schema = graphene.Schema(query=Query)

abc = "asd"
