from rest_framework import serializers
from django.db import transaction
from .models import GenreName, MovieDetail


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenreName
        fields = ('id', 'name')


class MovieDetailSerializer(serializers.ModelSerializer):
    """
        MovieSerializer for MovieDetails
    """
    genre = GenreSerializer(many=True)

    class Meta:
        model = MovieDetail
        fields = ('id', 'name', 'imdb_score', 'popularity', 'director', 'genre')


class AdminMovieSerializer(serializers.ModelSerializer):
    """
    """
    name = serializers.CharField(max_length=100, required=True)
    imdb_score = serializers.FloatField(required=True, min_value=0, max_value=10)
    popularity = serializers.FloatField(required=True, min_value=0, max_value=10)
    director = serializers.CharField(max_length=100, required=True)
    genre = serializers.ListField(required=True, min_length=1, max_length=5)

    class Meta:
        model = MovieDetail
        fields = ('name', 'imdb_score', 'popularity', 'director', 'genre')

    def to_representation(self, instance):

        response = super().to_representation(instance)
        return response

    @staticmethod
    def validate_name(name):
        """
            method used to validate the user name.
        :param name:
        :return:
        """
        if MovieDetail.objects.filter(name__exact=name).exists():
            raise serializers.ValidationError("Movie with same name already exist.")
        return name

    def create(self, validated_data):
        """
        Create and return a new `MovieDetail` instance, given the validated data.
        """
        with transaction.atomic():
            movie_genre = validated_data.pop('genre')
            movie = MovieDetail.objects.create(**validated_data)
            for name in movie_genre:
                genre, created = GenreName.objects.get_or_create(name=name)
                movie.genre.add(genre)
                movie.save()
            return movie

    def update(self, instance, validated_data):
        """
            update method used to update the MovieDetail instance
        :param instance:
        :param validated_data:
        :return:
        """
        with transaction.atomic():
            movie_genre = validated_data.get('genre')
            instance.imdb_score = validated_data.get('imdb_score')
            instance.popularity = validated_data.get('popularity')
            instance.director = validated_data.get('director')
            instance.save()
            for name in movie_genre:
                genre, created = GenreName.objects.get_or_create(name=name)
                instance.genre.add(genre)
                instance.save()
            return instance
