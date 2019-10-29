from flask import Flask
from flask_sqlalchemy import SQLAlchemy

DB_URI = "postgresql:///nullings"

db=SQLAlchemy()

class Post(db.Model):
    """A blog post."""

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    # Relationships
    contents = db.relationship("PostContent", backref="Post")

class PostContent(db.Model):
    """A blog post's content."""

    __tablename__ = "post_contents"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"))
    kind = db.Column(db.String(40), nullable=False)
    index = db.Column(db.Integer)

class Page(db.Model):
    """A static page."""

    __tablename__ = "pages"

    title = db.Column(db.String(40), primary_key=True)

    # Relationships
    contents = db.relationship("PageContent", backref="Page")
    
class PageContent(db.Model):
    """A page's contents."""

    __tablename__ = "page_contents"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    page = db.Column(db.String(40), db.ForeignKey("pages.title"))

def connect_to_db(app, database_uri):
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)

    db.create_all()
