from django.core.management.base import BaseCommand
import json
from django.conf import settings
from app.models import MovieDetail, GenreName


class Command(BaseCommand):
    help = 'Populate move from the json into table'

    @staticmethod
    def create_movie_genre(genre_list, movie):
        """
            method used to create movie genre
        :param genre_list:
        :param movie:
        :return:
        """
        for name in genre_list:
            genre, created = GenreName.objects.get_or_create(name=name)
            movie.genre.add(genre)
            movie.save()
        return True

    def create_movie_data(self, data):
        """
            method used to add movie in Movie table
        :param data:
        :return:
        """
        payload = dict()
        for movie_data in data:
            payload['name'] = movie_data.get('name')
            payload['popularity'] = movie_data.get('99popularity')
            payload['director'] = movie_data.get('director')
            payload['imdb_score'] = movie_data.get('imdb_score')
            movie, created = MovieDetail.objects.get_or_create(**payload)
            genre_list = movie_data.get('genre')
            self.create_movie_genre(genre_list, movie=movie)
        return True

    def handle(self, *args, **kwargs):
        file_path = settings.BASE_DIR + '/imdb.json'
        with open(file_path, 'r') as file:
            raw_data = file.read()
            data = json.loads(raw_data)
            self.create_movie_data(data)
        self.stdout.write("Data load successfully.")

