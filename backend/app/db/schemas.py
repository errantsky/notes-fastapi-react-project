from datetime import datetime
from pydantic import BaseModel
import typing as t





class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str = None
    permissions: str = "user"


class NoteBase(BaseModel):
    title: str
    text: str
    created: datetime
    last_edited: datetime


class NoteCreate(NoteBase):
    parent_folder_id: int

    class Config:
        orm_mode = True


class NoteEdit(NoteBase):
    parent_folder_id: int
    owner_id: int

    class Config:
        orm_mode = True


class Note(NoteBase):
    id: int
    parent_folder_id: int
    owner_id: int

    class Config:
        orm_mode = True


class FolderBase(BaseModel):
    name: str
    # ToDo: Add sort type


class FolderCreate(FolderBase):
    class Config:
        orm_mode = True

class FolderEdit(FolderBase):
    class Config:
        orm_mode = True

class Folder(FolderBase):
    id: int
    owner_id: int
    notes: t.List[Note] = []

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    is_active: bool = True
    is_superuser: bool = False
    first_name: str = None
    last_name: str = None


class UserOut(UserBase):
    pass


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserEdit(UserBase):
    password: t.Optional[str] = None

    class Config:
        orm_mode = True


class User(UserBase):
    id: int
    notes: t.List[Note] = []
    folders: t.List[Folder] = []

    class Config:
        orm_mode = True
