from typing import List, Optional
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserSchema(UserBase):
    password: str


class FeedSchema(BaseModel):
    user_id: int
    url_rss: str
    title: str

# class User(UserBase):
#     id: int
#     is_active: bool
#
#     class Config:
#         orm_mode = True
