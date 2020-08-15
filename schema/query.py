import graphene

from utils import read_rss
from .types import Feed, FeedSummary
from schemas import UserSchema
from database import Session
import crud


class Query(graphene.ObjectType):
    feed = graphene.List(Feed, rss_id=graphene.Int())
    login = graphene.Int(email=graphene.String(),
                         password=graphene.String())
    get_feeds_by_user = graphene.List(FeedSummary, user_id=graphene.Int())

    def resolve_feed(self, info, rss_id: int):
        entry = crud.get_feed_by_rss_id(Session, rss_id)
        return entry

    def resolve_login(self, info, email: str, password: str):
        schema_user = UserSchema(email=email, password=password)
        user_create = crud.get_user(Session, schema_user)
        return user_create

    def resolve_get_feeds_by_user(self, info, user_id: int):
        rss = crud.get_rss_by_user_id(Session, user_id)
        return [{'url_rss': rs.url_rss, 'title': rs.title, 'id': rs.id} for rs in rss]
