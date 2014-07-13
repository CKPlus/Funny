from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from my_sites.tikann.database import Base
# from my_sites import db

class User(Base):
    __tablename__ = 'test_users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    url = Column(String(200))
    likes = Column(Integer)
    publish_date = Column(String(50))
    author = Column(String(50))
    content = relationship('Image', backref='article')


class Image(Base):
    __tablename__ = 'image'
    id = Column(Integer, primary_key=True)
    url = Column(String(50))
    article_id = Column(Integer, ForeignKey('article.id'))
