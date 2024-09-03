"""Modelo para la aplicación"""
class Movie:
    """Clase que representa una película."""
    def __init__(self, id, title, overview, poster_path, release_date, vote_average):
        self.id = id
        self.title = title
        self.overview = overview
        self.poster_path = poster_path
        self.release_date = release_date
        self.vote_average = vote_average

    def to_dict(self):
        """Convierte el objeto Movie a un diccionario"""
        return {
            'id': self.id,
            'title': self.title,
            'overview': self.overview,
            'poster_path': self.poster_path,
            'release_date': self.release_date,
            'vote_average': self.vote_average
        }
