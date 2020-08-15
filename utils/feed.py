import models
from utils import read_rss
import crud
from database import Session
import schemas
import logging

logger = logging.getLogger(__name__)


def save_feed(db: Session, rs: models.Rss):
    responses = []
    for i in range(3):
        responses = read_rss(rs.url_rss)
        if responses:
            break

    if responses:
        for response in responses:
            feed_schema = schemas.FeedSchema(title=response['title'],
                                             summary=response['summary'],
                                             published=response.get('published', None),
                                             image=response['image'],
                                             author=response['author'], link=response['link'],
                                             id_feed=response['id_feed'], rss_id=rs.id)
            crud.save_feed(db, feed_schema)
    else:
        logger.error(f'NO SE PUDO ACTUALIZAR EL FEED : {rs.url_rss} , con el id : {rs.id}')


def save_feeds(db: Session):
    rss = crud.get_rss_all(db)
    for rs in rss:
        save_feed(db, rs)


async def update_feeds():
    while True:
        save_feeds(Session)
