from app.classes.db import db
from sqlalchemy.sql import func
from flask_jwt import current_identity
import hashlib


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=20), unique=True, nullable=False)
    password = db.Column(db.String(length=255), nullable=False)
    first_name = db.Column(db.String(length=20), nullable=False)
    last_name = db.Column(db.String(length=20), nullable=False)
    active = db.Column(db.Boolean(), default=0, nullable=True)
    created_date = db.Column(db.DateTime(timezone=True), default=func.now(), nullable=False)

    def __init__(self, username, password, first_name, last_name, active=0):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.active = active

    def json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'active': self.active,
            'created_date': self.created_date.strftime("%Y-%m-%d, %I:%M:%S")
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_password_hash(cls, password):
        h = hashlib.md5(password.encode())
        return h.hexdigest()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def get_current_identity_user_id(cls):
        return '%d' % current_identity.get('id')

    @classmethod
    def get_current_identity_user(cls):
        user_id = '%d' % current_identity.get('id')
        user = cls.find_by_id(user_id)
        return user.json()
