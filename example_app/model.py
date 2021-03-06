from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from copy import deepcopy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(60), nullable=False)
    user_password = db.Column(db.String(128), nullable=False)
    user_email = db.Column(db.String(30), nullable=False, unique=True)
    articles = db.relationship("Article", backref="user")
    comments = db.relationship("Comment", backref="user")   

    def __repr__(self):
        return self.user_name

    def __init__(self, data):
        for item in data.items():
            setattr(self, item[0], item[1])

    def to_json(self):
        dic = deepcopy(self.__dict__)
        dic.pop('_sa_instance_state', None)
        return dic

    def update(self, data):
        for item in data.items():
            setattr(self, item[0], item[1])
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()


class Article(db.Model):
    __tablename__ = "article"
    article_id = db.Column(db.Integer, primary_key=True)
    article_title = db.Column(db.String(50), nullable=False)
    article_content = db.Column(db.String(5000), nullable=False)
    article_date = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))
    click = db.Column(db.Integer, default=0)
    comments = db.relationship("Comment", backref="article", lazy='dynamic')
    
    def __repr__(self):
        return self.article_title

    def __init__(self, data):
        for item in data.items():
            setattr(self, item[0], item[1])

    def to_json(self):
        dic = deepcopy(self.__dict__)
        dic.pop('_sa_instance_state', None)
        dic['article_date'] = dic['article_date'].strftime('%Y-%m-%d %H:%M:%S')
        return dic

    def update(self, data):
        for item in data.items():
            setattr(self, item[0], item[1])
        try:
            db.session.add(self)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()


class Comment(db.Model):
    __tablename__ = "comment"
    comment_id = db.Column(db.Integer, primary_key=True)
    comment_content = db.Column(db.String(500), nullable=False)
    comment_date = db.Column(db.DateTime, default=datetime.utcnow())
    article_id = db.Column(db.Integer, db.ForeignKey("article.article_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.user_id"))

    def __repr__(self):
        return self.comment_content

    def __init__(self, data):
        for item in data.items():
            setattr(self, item[0], item[1])

    def to_json(self):
        dic = deepcopy(self.__dict__)
        dic.pop('_sa_instance_state', None)
        dic['comment_date'] = dic['comment_date'].strftime('%Y-%m-%d %H:%M:%S')
        return dic