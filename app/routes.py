
from flask import Blueprint, jsonify, current_app
import requests

bp = Blueprint('main', __name__)

@bp.route('/')
def home():
    return "Yo soy home"

@bp.route('/movies')
def movies():
    api_key = current_app.config['TMDB_API_KEY']
    url = f'https://api.themoviedb.org/3/movie/popular?api_key={api_key}&language=en-US&page=1'
    response = requests.get(url)
    data = response.json()
    movies_data = data.get('results', [])
    return jsonify(movies_data)

@bp.route('/movies/<int:id>')
def movie_detail(id):
    api_key = current_app.config['TMDB_API_KEY']
    url = f'https://api.themoviedb.org/3/movie/{id}?api_key={api_key}&language=en-US'
    response = requests.get(url)
    movie_detail_data = response.json()
    return jsonify(movie_detail_data)
