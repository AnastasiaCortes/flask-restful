from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from code.item import Item, ItemList
from code.security import authenticate, identity
from code.user import UserRegister

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = "anastasia"
api = Api(app)

jwt = JWT(app, authenticate, identity)   # /auth


api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == "__main__":
    app.run(port=5000)
