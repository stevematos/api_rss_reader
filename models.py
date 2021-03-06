from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class Rss(Base):
    __tablename__ = "rss"

    id = Column(Integer, primary_key=True, index=True)
    url_rss = Column(String, index=True)
    title = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship("User")


class Feed(Base):
    __tablename__ = "feed"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    summary = Column(String)
    published = Column(DateTime)
    image = Column(String)
    author = Column(String)
    link = Column(String)
    id_feed = Column(String)
    rss_id = Column(Integer, ForeignKey('rss.id'))
    rss = relationship("Rss")
