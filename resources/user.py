from flask import Blueprint, Response, request
from flask_jwt_extended import create_access_token
from database.models import User
import datetime

users = Blueprint('users', __name__)

@users.route('/users')
def get_users():
    users = User.objects().to_json()
    return Response(users, mimetype="application/json", status=200)

@users.route('/users', methods=['POST'])
def sign_up():
	body = request.get_json()
	user = User(**body).save()
	user.hash_password()
	user.save()
	id = user.id
	return {'id': str(id)}, 200

@users.route('/users/login', methods=['POST'])
def sign_in():
	body = request.get_json()
	user = User.objects.get(email=body.get('email'))
	authorized = user.check_password(body.get('password'))
	if not authorized:
		return {'error': 'Email or password invalid'}, 401

	expires = datetime.timedelta(days=7)
	access_token = create_access_token(identity=str(user.id), expires_delta=expires)
	return {'token': access_token}, 200
