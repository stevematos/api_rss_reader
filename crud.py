from sqlalchemy.orm import Session

import models
import schemas

import bcrypt


#
#
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserSchema) -> models.User:
    hashed_password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user: schemas.UserSchema):
    db_user: models.User = get_user_by_email(db, user.email)
    if db_user:
        if bcrypt.checkpw(user.password.encode('utf-8'), db_user.hashed_password):
            return db_user.id
        else:
            return False
    else:
        return False


def get_rss_by_url(db: Session, url: str, user_id: int):
    return db.query(models.Rss).filter(models.Rss.url_rss == url,
                                       models.Rss.user_id == user_id).first()


def subscribe_rss(db: Session, rss: schemas.RssSchema):
    db_rss = models.Rss(**rss.dict())
    db.add(db_rss)
    db.commit()
    db.refresh(db_rss)
    return db_rss


def get_rss_by_user_id(db: Session, user_id: int):
    return db.query(models.Rss).filter(models.Rss.user_id == user_id).all()


def get_rss_all(db: Session):
    return db.query(models.Rss).filter().all()


def get_feed_by_rss_id(db: Session, rss_id: int):
    return db.query(models.Feed).filter(models.Feed.rss_id == rss_id).all()


def get_feed_by_id_feed(db: Session, rss_id: int, id_feed: str):
    return db.query(models.Feed).filter(models.Feed.rss_id == rss_id,
                                        models.Feed.id_feed == id_feed).first()


def save_feed(db: Session, feed: schemas.FeedSchema):
    if not get_feed_by_id_feed(db, feed.rss_id, feed.id_feed):
        db_feed = models.Feed(**feed.dict())
        db.add(db_feed)
        db.commit()
        db.refresh(db_feed)
        return db_feed
    else:
        return False


def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()


def delete_rss(db: Session, rss_id: int):
    db.query(models.Rss).filter(models.Rss.id == rss_id).delete()
    db.commit()


def delete_feeds_by_rss_id(db: Session, rss_id: int):
    db.query(models.Feed).filter(models.Feed.rss_id == rss_id).delete()
    db.commit()
