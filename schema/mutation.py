import graphene
from graphql import GraphQLError

import crud
from fastapi import Depends, HTTPException
from .types import User
from schemas import UserSchema, FeedSchema
from database import Session


class CreateUser(graphene.Mutation):
    class Arguments:
        email = graphene.String()
        password = graphene.String()

    user = graphene.Field(User)

    def mutate(self, info, email: str, password: str):
        db_user = crud.get_user_by_email(Session, email=email)
        if db_user:
            raise GraphQLError("Email ya esta registrado")
        schema_user = UserSchema(email=email, password=password)
        user_create = crud.create_user(Session, schema_user)
        dict_user = {
            'id': user_create.id,
            'email': user_create.email
        }
        return CreateUser(user=User(**dict_user))


class SubscribeFeed(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int()
        url_feed = graphene.String()
        title = graphene.String()

    id_feed = graphene.Int()

    def mutate(self, info, user_id: int, url_feed: str, title: str):
        db_feed = crud.get_feed_by_url(Session, url=url_feed, user_id=user_id)
        if db_feed:
            raise GraphQLError("Feed ya esta creado")
        schema_feed = FeedSchema(user_id=user_id, url_rss=url_feed, title=title)
        feed_create = crud.subscribe_feed(Session, schema_feed)
        return SubscribeFeed(id_feed=feed_create.id)


class Mutation(graphene.ObjectType):
    CreateUser = CreateUser.Field()
    SubscribeFeed = SubscribeFeed.Field()
