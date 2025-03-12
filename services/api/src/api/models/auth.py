# PYTHON IMPORTS
from datetime import datetime
from typing import List

# LIBRAY IMPORTS
from beanie import (
    Delete,
    Document,
    Insert,
    PydanticObjectId,
    SaveChanges,
    Update,
    after_event,
    before_event,
)
from pydantic import BaseModel, Field
import bcrypt

# LOCAL IMPORTS
from api.models.defaults import utc_future_days, utc_now, uuid


class UserGroup(Document):
    user: PydanticObjectId
    group: PydanticObjectId
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)

    @before_event(Update, SaveChanges)
    async def update_last(self):
        self.updated = utc_now()


class Group(Document):
    name: str
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)

    @before_event(Update, SaveChanges)
    async def update_last(self):
        self.updated = utc_now()

    @before_event(Delete)
    async def remove_related(self):
        await UserGroup.find_all(UserGroup.group == self.id).delete()


class User(Document):
    username: str
    email: str | None = None
    full_name: str | None = None
    disabled: bool = False
    password: str
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)

    class Config:
        json_schema_extra = {
            "examples": [
                {
                    "username": "Username",
                    "email": "Email@email.com",
                    "full_name": "First Name Surname",
                }
            ]
        }

    @before_event(Update, SaveChanges, Insert)
    async def update_last(self):
        salt = bcrypt.gensalt()
        self.password = bcrypt.hashpw(self.password.encode("utf-8"), salt).decode(
            "utf-8"
        )
        self.updated = utc_now()

    async def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    @after_event(Delete)
    async def remove_related(self):
        await UserGroup.find_all(UserGroup.user == self.id).delete()
        await Token.find_all(Token.user == self.id).delete()


class Token(Document):
    user: PydanticObjectId
    host: str
    session: str = ""
    code: str = Field(default_factory=uuid)
    scopes: List[str] = []
    created: datetime = Field(default_factory=utc_now)
    updated: datetime = Field(default_factory=utc_now)
    expiration: datetime = Field(default_factory=utc_future_days)

    @before_event(Update, SaveChanges)
    async def update_last(self):
        self.updated = utc_now()


class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str
    name: str = ""
