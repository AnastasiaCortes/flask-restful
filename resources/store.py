from flask_restful import Resource

from models.store import StoreModel


class Store(Resource):
    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': f"A store with name {name} already exists!"}, 400  # if the name is already in database we return an error 404

        store = StoreModel(name)
        try:
            store.save_to_db()
        except:
            return {'message': "An error occurred while creating the store"}, 500  # internal server error

        return store.json(), 201

    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': "Store not found"}, 404

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': "Store has been deleted"}


class StoreList(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}