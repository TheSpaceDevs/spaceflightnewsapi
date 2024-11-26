#  type: ignore

from graphene import ObjectType, Schema

from api.schema import Query as ApiQuery


class Query(ApiQuery, ObjectType):
    pass


schema = Schema(query=Query)
