import graphene
from utils import read_rss
from .types import Feed, FeedSummary
from schemas import UserSchema
from database import Session
import crud


class Query(graphene.ObjectType):
    feed = graphene.List(Feed, url=graphene.String())
    login = graphene.Int(email=graphene.String(),
                         password=graphene.String())
    get_feeds_by_user = graphene.List(FeedSummary, user_id=graphene.Int())

    def resolve_feed(self, info, url: str):
        entry = read_rss(url)
        return entry

    def resolve_login(self, info, email: str, password: str):
        schema_user = UserSchema(email=email, password=password)
        user_create = crud.get_user(Session, schema_user)
        return user_create

    def resolve_get_feeds_by_user(self, info, user_id: int):
        feeds = crud.get_feeds_by_user_id(Session, user_id)
        return [{'url_rss': feed.url_rss, 'title': feed.title} for feed in feeds]
