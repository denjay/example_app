from flask import request, g, url_for
from flask_restful import reqparse

from . import Resource
from .. import schemas
from model import db, User, Article
from ..auths import Auth

parser = reqparse.RequestParser()
parser.add_argument('user_name', type=str, help='用户名')
parser.add_argument('user_password', type=str, help='密码')
parser.add_argument('email', type=str, help='电子邮箱')


class Users(Resource):

    def get(self):
        users = User.query.all()
        return [user.to_json() for user in users]


class Users_id(Resource):

    def get(self, user_id):
        user = User.query.filter_by(user_id=user_id).first()
        return user.to_json()

    @Auth.login_required
    def put(self, user_id):
        """修改用户资料"""
        user = User.query.filter_by(user_id=user_id).first_or_404()
        try:
            user.update(request.form.to_dict())
        except:
            return {'message': False}
        return {'messige': True}


class Users_id_articles(Resource):

    def get(self, user_id):
        user = User.query.filter_by(user_id=user_id).first()
        articles = user.articles
        return [article.to_json() for article in articles]


class Login(Resource):

    def post(self):
        args = parser.parse_args()
        username = args['user_name']
        password = args['user_password']
        user = User.query.filter_by(user_name=username).first_or_404()
        if user.user_password == password:
            token = Auth.encode_auth_token(user.user_id)
            return {'result': '登录成功'}, 200, {"authorization": "Bearer " + str(token)}


class Register(Resource):

    def post(self):
        data = request.form
        data = data.to_dict()
        user = User(data)
        try:
            db.session.add(user)
            db.session.commit()
        except:
            db.session.rollback()
            db.session.flush()
            return {'error': '注册失败'}
        return data
