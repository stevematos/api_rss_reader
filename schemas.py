from typing import List, Optional, Any
from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    email: str


class UserSchema(UserBase):
    password: str


class RssSchema(BaseModel):
    user_id: int
    url_rss: str
    title: str


class FeedSchema(BaseModel):
    title: str
    summary: str
    published: Any
    image: str
    author: str
    link: str
    id_feed: str
    rss_id: int

# class User(UserBase):
#     id: int
#     is_active: bool
#
#     class Config:
#         orm_mode = True
