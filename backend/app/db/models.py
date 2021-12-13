from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .session import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    notes = relationship('Note', back_populates="owner")
    folders = relationship('Folder', back_populates="owner")


class Folder(Base):
    __tablename__ = 'folder'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    owner_id = Column(Integer, ForeignKey('user.id'))

    notes = relationship("Note", back_populates="parent_node")
    owner = relationship('User', back_populates="folders")


class Note(Base):
    __tablename__ = 'note'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    text = Column(String)
    created = Column()
    last_edited = Column()
    parent_folder_id = Column(Integer, ForeignKey('folder.id'))
    owner_id = Column(Integer, ForeignKey('user.id'))

    parent_folder = relationship('Folder', back_populates="notes")
    owner = relationship('User', back_populates="notes")
