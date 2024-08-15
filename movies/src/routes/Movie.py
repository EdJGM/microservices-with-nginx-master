from flask import Blueprint, jsonify, request
import uuid

# Entities
from models.entities.Movie import Movie
# Models
from models.movieModel import MovieModel

main = Blueprint('movie_blueprint', __name__)

@main.route('/')
def get_movies():
    try:
        movies = MovieModel.get_movies()
        return jsonify(movies)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@main.route('/<id>')
def get_movie(id):
    try:
        movie = MovieModel.get_movie(id)
        if movie is not None:
            return jsonify(movie)
        else:
            return jsonify({'error': 'Movie not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@main.route('/add', methods=['POST'])
def add_movie():
    try:
        titulo = request.json['titulo']
        duracion = int(request.json['duracion'])
        fecha_estreno = request.json['fecha_estreno']
        id = uuid.uuid4()
        movie = Movie(str(id), titulo, duracion, fecha_estreno)
        affected_rows = MovieModel.add_movie(movie)

        if affected_rows == 1:
            return jsonify({'message': 'Movie added successfully'})
        else:
            return jsonify({'error': 'An error occurred while adding the movie'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@main.route('/update/<id>', methods=['PUT'])
def update_movie(id):
    try:
        titulo = request.json['titulo']
        duracion = int(request.json['duracion'])
        fecha_estreno = request.json['fecha_estreno']
        movie = Movie(id, titulo, duracion, fecha_estreno)

        affected_rows = MovieModel.update_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "No movie updated"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500


@main.route('/delete/<id>', methods=['DELETE'])
def delete_movie(id):
    try:
        movie = Movie(id)

        affected_rows = MovieModel.delete_movie(movie)

        if affected_rows == 1:
            return jsonify(movie.id)
        else:
            return jsonify({'message': "No movie deleted"}), 404

    except Exception as ex:
        return jsonify({'message': str(ex)}), 500