from copy import deepcopy
from datetime import datetime
from flask import request, jsonify
from model import db, Article, Comment
from ..auths import Auth
from . import Resource
from .. import schemas


class Articles(Resource):

    def get(self):
        articles = Article.query.all()
        # return jsonify([article.to_json() for article in articles])
        articles_json = []
        for article in articles:
            article_json = article.to_json()
            article_json["article_content"] = article_json["article_content"][0:200]
            articles_json.append(article_json)
        return jsonify(articles_json)


    @Auth.login_required
    def post(self):
        auth_token = request.headers.get("Authorization")
        payload = Auth.decode_auth_token(auth_token)
        if payload is False:
            return {'message': '无效令牌'}, 401
        user_id = payload["data"]['id']
        data = eval(request.data)
        data['user_id'] = user_id
        try:
            article = Article(data)
            db.session.add(article)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()
            return {'message': '文章提交失败'}, 400
        return {'message': '文章提交成功！'}


class Articles_hot(Resource):

    def get(self):
        articles = Article.query.order_by(-Article.click).limit(8)
        return jsonify([article.to_json() for article in articles])


class Articles_id(Resource):

    def get(self, articles_id):
        article = Article.query.filter_by(article_id=articles_id).first_or_404()
        # 由于提交article到数据库的操作会改变article属性，所以先深拷贝一份article对象
        article_copy = deepcopy(article)
        article.click = article.click + 1
        db.session.add(article)
        db.session.commit()
        return article_copy.to_json()

    @Auth.login_required
    def delete(self, articles_id):
        auth_token = request.headers.get("Authorization")[7:]
        payload = Auth.decode_auth_token(auth_token)
        if payload is False:
            return {'message': '无效令牌'}, 401
        user_id = payload["data"]['id']
        article = Article.query.filter_by(id=articles_id).first_or_404()
        if article.user_id == user_id:
            db.session.delete(article)
            return {'message': '文章删除成功！'}
        return {'message': '文章删除失败！'}, 400


class Articles_id_comments(Resource):

    def get(self, article_id):
        article = Article.query.filter_by(article_id=article_id).first_or_404()
        comments = article.comments.order_by(Comment.comment_date)
        comments_json = []
        for comment in comments:
            comment_json = comment.to_json()
            comment_json.update({"user_name": comment.user.user_name})
            comments_json.append(comment_json)
        return comments_json
    
    @Auth.login_required
    def post(self, article_id):
        # 令牌要去掉前面的Bearer字符
        auth_token = request.headers.get("Authorization")[7:]
        payload = Auth.decode_auth_token(auth_token)
        if payload is False:
            return {'message': '无效令牌'}, 401
        user_id = payload["data"]['id']
        data = eval(request.data)
        data.update({'user_id': user_id, 'article_id': article_id, 'comment_date': datetime.utcnow()})
        try:
            comment = Comment(data)
            comment_json = comment.to_json()
            db.session.add(comment)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()
            return {'message': '评论提交失败'}, 400
        return comment_json
        