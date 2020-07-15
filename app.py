from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item, ItemList
from resources.store import StoreList, Store
from security import authenticate, identity
from resources.user import UserRegister
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "anastasia"
api = Api(app)


jwt = JWT(app, authenticate, identity)   # /auth


api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')


if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)

