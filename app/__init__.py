import datetime
from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flask_migrate import Migrate
from app.classes.config import config
from app.classes.db import db

from app.classes.security import authenticate, identity
from app.resources.user import UserRegister, UserList, UserInfo, UserIdentity
from app.resources.backups import BackupsList
from app.resources.restore import ProcessBackupFile


app = Flask(__name__)
app.debug = True
app.config['SQLALCHEMY_DATABASE_URI'] = config.get('api_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPOGATE_EXCEPTIONS'] = True
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(hours=3)
app.secret_key = config.get('api_secret')
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth


@jwt.jwt_error_handler
def error_handler(e):
    app.logger.error("ERROR: ", "JWT error Something bad happened")
    return "Something bad happened", 500



migrate = Migrate(app, db)

db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


api.add_resource(UserList, '/users')
api.add_resource(UserInfo, '/user/<string:username>')
api.add_resource(UserIdentity, '/user/identity')
api.add_resource(UserRegister, '/register')
