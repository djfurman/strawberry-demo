import typing
from datetime import datetime

import strawberry

from .models import User


def get_books():
    return [Book(title="Functional Python", author="Steve Lott")]


def get_users():
    return [User(id=1, name="me", signup_ts=datetime.utcnow())]


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.experimental.pydantic.type(model=User, all_fields=True)
class UserGqlType:
    pass


@strawberry.type
class Query:
    books: typing.List[Book] = strawberry.field(resolver=get_books)
    users: typing.List[UserGqlType] = strawberry.field(resolver=get_users)


schema = strawberry.Schema(query=Query)
