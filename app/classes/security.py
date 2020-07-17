from werkzeug.security import safe_str_cmp
from app.models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, UserModel.get_password_hash(password)) and user.active:
        return user
    return None


def identity(payload):
    user_id = payload['identity']
    user = UserModel.find_by_id(user_id)
    return user.json()

