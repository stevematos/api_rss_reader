import graphene


class FeedSummary(graphene.ObjectType):
    title = graphene.String()
    url_rss = graphene.String()
    id = graphene.Int()


class Feed(graphene.ObjectType):
    title = graphene.String()
    summary = graphene.String()
    published = graphene.DateTime()
    image = graphene.String()
    author = graphene.String()
    link = graphene.String()


class User(graphene.ObjectType):
    id = graphene.Int()
    email = graphene.String()
