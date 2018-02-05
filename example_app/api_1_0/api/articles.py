from flask import request, g
from model import db, Article
from ..auths import Auth
from . import Resource
from .. import schemas


class Articles(Resource):

    def get(self):
        articles = Article.query.all()
        return [article.to_json() for article in articles]

    @Auth.login_required
    def post(self):
        auth_token = request.headers.get("Authorization")
        payload = Auth.decode_auth_token(auth_token)
        if payload is False:
            return {'message': '无效令牌'}
        user_id = payload["data"]['id']
        data = request.form.to_dict()
        print(data)
        data['user_id'] = user_id
        try:
            article = Article(data)
            db.session.add(article)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()
            return {'message': '文章提交失败'}
        return {'message': '文章提交成功！'}


class Articles_id(Resource):

    @Auth.login_required
    def delete(self, articles_id):
        pass
        auth_token = request.headers.get("Authorization")
        payload = Auth.decode_auth_token(auth_token)
        if payload is False:
            return {'message': '无效令牌'}
        user_id = payload["data"]['id']
        article = Article.query.filter_by(id=articles_id).first_or_404()
        if article.user_id == user_id:
            db.session.delete(article)
            return {'message': '文章删除成功！'}
        return {'message': '文章删除失败！'}
