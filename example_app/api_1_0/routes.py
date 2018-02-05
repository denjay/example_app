###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from .api.articles import Articles, Articles_id
from .api.user import Users, Users_id, Login, Register, Users_id_articles

routes = [
    dict(resource=Articles, urls=['/articles'], endpoint='articles'),
    dict(resource=Articles_id, urls=['/articles/<int:articles_id>'], endpoint='articles_id'),
    dict(resource=Users, urls=['/users'], endpoint='users'),
    dict(resource=Users_id, urls=['/users/<int:user_id>'], endpoint='users_id'),
    dict(resource=Login, urls=['/login'], endpoint='login'),
    dict(resource=Register, urls=['/register'], endpoint='Register'),
    dict(resource=Users_id_articles, urls=['/users/<int:user_id>/articles'], endpoint='users_id_articles'),
]
