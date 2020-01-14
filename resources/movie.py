from flask import Blueprint, Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Movie, User

movies = Blueprint('movies', __name__)

@movies.route('/movies')
@jwt_required
def get_movies():
    movies = Movie.objects().to_json()
    return Response(movies, mimetype="application/json", status=200)

@movies.route('/movies', methods=['POST'])
@jwt_required
def add_movie():
    user_id = get_jwt_identity()
    body = request.get_json()
    user = User.objects.get(id=user_id)
    movie = Movie(**body, added_by=user)
    movie.save()
    user.update(push__movies=movie)
    user.save()
    id = movie.id
    return {'id': str(id)}, 200

@movies.route('/movies/<id>', methods=['PUT'])
@jwt_required
def update_movie(id):
    user_id = get_jwt_identity()
    movie = Movie.objects.get(id=id, added_by=user_id)
    body = request.get_json()
    Movie.objects.get(id=id).update(**body)
    return '', 200

@movies.route('/movies/<id>', methods=['DELETE'])
@jwt_required
def delete_movie(id):
    user_id = get_jwt_identity()
    movie = Movie.objects.get(id=id, added_by=user_id)
    movie.delete()
    return '', 200

@movies.route('/movies/<id>')
@jwt_required
def get_movie(id):
    movies = Movie.objects.get(id=id).to_json()
    return Response(movies, mimetype="application/json", status=200)