import os
import sys
import enum
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250))

class Follower(Base):
    __tablename__ = 'follower'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.ID'))
    user_to_id = Column(Integer, ForeignKey('user.ID'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'post'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.ID'))
    user = relationship(User)

class MediaType(enum.Enum):
    IMAGE = "image"
    VIDEO = "video"
    GIF = "gif"

class Media(Base):
    __tablename__ = 'media'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    type = Column(Enum(MediaType), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.ID'))
    post = relationship(Post)

class Comment(Base):
    __tablename__ = 'comment'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    ID = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('user.ID'))
    user = relationship(User)
    post_id = Column(Integer, ForeignKey('post.ID'))
    post = relationship(Post)

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
