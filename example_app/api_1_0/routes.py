###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from .api.articles import Articles
from .api.user import Users, Users_id

routes = [
    dict(resource=Articles, urls=['/articles'], endpoint='articles'),
    dict(resource=Users, urls=['/users'], endpoint='users'),
    dict(resource=Users_id, urls=['/users/<int:id>'], endpoint='users_id'),
]
