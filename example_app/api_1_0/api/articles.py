from flask import request, g

from . import Resource
from .. import schemas


class Articles(Resource):

    def get(self):

        return [], 200, None