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


def get_feed_by_url(db: Session, url: str, user_id: int):
    return db.query(models.Feed).filter(models.Feed.url_rss == url,
                                        models.Feed.user_id == user_id).first()


def subscribe_feed(db: Session, feed: schemas.FeedSchema):
    db_feed = models.Feed(**feed.dict())
    db.add(db_feed)
    db.commit()
    db.refresh(db_feed)
    return db_feed


def get_feeds_by_user_id(db: Session, user_id: int):
    return db.query(models.Feed).filter(models.Feed.user_id == user_id).all()
