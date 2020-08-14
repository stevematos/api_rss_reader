from sqlalchemy.orm import Session
import models


def delete_user(db: Session, user_id: int):
    db.query(models.User).filter(models.User.id == user_id).delete()
    db.commit()


def delete_feed(db: Session, feed_id: int):
    db.query(models.Feed).filter(models.Feed.id == feed_id).delete()
    db.commit()
