"""Rutas de movieApp"""
from flask import Blueprint, jsonify, current_app
import requests
from .models import Movie
bp = Blueprint('main', __name__)

@bp.route('/movies')
def movies():
    api_key = current_app.config['TMDB_API_KEY']
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url, timeout=10)
    data = response.json()
    movies_data = data.get('results', [])

    # Usar el modelo para transformar los datos
    movies_list = [Movie(
        id=m['id'],
        title=m['title'],
        overview=m['overview'],
        poster_path=f"https://image.tmdb.org/t/p/w500{m['poster_path']}",
        release_date=m['release_date'],
        vote_average=m['vote_average']
    ) for m in movies_data]

    # Convertir los objetos Movie a diccionarios para enviar como JSON
    return jsonify([movie.to_dict() for movie in movies_list])

@bp.route('/movies/<int:id>')
def movie_detail(id):
    api_key = current_app.config['TMDB_API_KEY']
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key={api_key}&language=en-US'
    response = requests.get(url, timeout=10)
    movie_detail_data = response.json()

    # Usar el modelo para transformar los datos
    movie = Movie(
        id=movie_detail_data['id'],
        title=movie_detail_data['title'],
        overview=movie_detail_data['overview'],
        poster_path=f"https://image.tmdb.org/t/p/w500{movie_detail_data['poster_path']}",
        release_date=movie_detail_data['release_date'],
        vote_average=movie_detail_data['vote_average']
    )

    return jsonify(movie.to_dict())

