from flask import request, g, jsonify, url_for

from . import Resource
from .. import schemas
from model import db, User


class Users(Resource):

    def get(self):
        users = User.query.all()
        return [user.to_json() for user in users]

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
            return {'error': '更新失败'}
        return data


class Users_id(Resource):

    def get(self, id):
        user = User.query.filter_by(user_id=id).first()
        return user.to_json()

    def put(self, id):
        user = User.query.filter_by(user_id=id).first_or_404()
        user.update(request.form.to_dict())
        return user.to_json()
