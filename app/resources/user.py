from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from app.models.user import UserModel


class UserList(Resource):

    @jwt_required()
    def get(self):
        return {'users': list(map(lambda x: x.json(), UserModel.query.all()))}


class UserIdentity(Resource):
    @jwt_required()
    def get(self):
        return UserModel.get_current_identity_user()


class UserInfo(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'password',
        type=str
    )
    parser.add_argument(
        'first_name',
        type=str
    )
    parser.add_argument(
        'last_name',
        type=str
    )
    parser.add_argument(
        'active',
        type=int
    )

    @jwt_required()
    def get(self, username):
        user = UserModel.find_by_username(username)
        if user:
            return user.json()
        return {'message': "User not found"}, 404

    @jwt_required()
    def post(self, username):
        if UserModel.find_by_username(username):
            return {'message': "A user with the username '{}' already exists.".format(username)}, 400

        data = UserInfo.parser.parse_args()

        data['password'] = UserModel.get_password_hash(data['password'])

        user = UserModel(username, data['password'], data['first_name'], data['last_name'], data['active'])

        try:
            user.save_to_db()
        except:
            return {'message': "An error occurred while inserting the user."}, 500

        return user.json(), 201

    @jwt_required()
    def put(self, username):
        data = UserInfo.parser.parse_args()

        user = UserModel.find_by_username(username)

        if user:
            if data['password']:
                data['password'] = UserModel.get_password_hash(data['password'])
                user.password = data['password']
            if data['first_name']:
                user.first_name = data['first_name']
            if data['last_name']:
                user.last_name = data['last_name']
            if data['active']:
                user.active = data['active']
        else:
            if data['password']:
                data['password'] = UserModel.get_password_hash(data['password'])
            user = UserModel(username, data['password'], data['first_name'], data['last_name'], data['active'])

        user.save_to_db()

        return user.json()

    @jwt_required()
    def delete(self, username):
        user = UserModel.find_by_username(username)
        if user:
            user.delete_from_db()
            return {'message': 'User deleted.'}
        return {'message': 'User not found.'}, 404


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'username',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'password',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'first_name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument(
        'last_name',
        type=str,
        required=True,
        help="This field cannot be left blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}, 400

        data['password'] = UserModel.get_password_hash(data['password'])
        user = UserModel(**data)

        try:
            user.save_to_db()
        except:
            return {'message': "An error occurred while inserting the user."}, 500

        return {"message": "User created successfully."}, 201
