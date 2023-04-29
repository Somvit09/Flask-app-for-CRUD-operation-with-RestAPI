from flask import Flask, jsonify, request
import mongoengine
from flask_restful import Api, Resource

# configuring app
app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'test-flask',
    'host': 'mongodb://localhost:27017/mydatabase'
}

# configuring database
mongoengine.connect('test-flask', host='mongodb://localhost:27017/mydatabase')

api = Api(app)

# define the User model
class User(mongoengine.Document):
    name = mongoengine.StringField(required=True)
    email = mongoengine.EmailField(required=True)
    password = mongoengine.StringField(required=True)

# define the User resource
class UserResource(Resource):
    def get(self, user_id=None):
        if user_id:
            user = User.objects.get(id=user_id)
            user_dict = {'id': str(user.id), 'name': user.name, 'email': user.email}
            return jsonify({'result': user_dict})
        else:
            users = User.objects()
            users_list = [{'id': str(user.id), 'name': user.name, 'email': user.email} for user in users]
            return jsonify({'result': users_list})

    def post(self):
        user = User(**request.json).save()
        return jsonify({'result': str(user.id)})

    def put(self, user_id):
        user = User.objects.get(id=user_id)
        user.update(**request.json)
        return jsonify({'result': str(user.id)})

    def delete(self, user_id):
        user = User.objects.get(id=user_id)
        user.delete()
        return jsonify({'result': str(user.id)})

api.add_resource(UserResource, '/users', '/users/<string:user_id>')

if __name__ == '__main__':
    app.run(debug=True, port=8000)

