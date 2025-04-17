from rest_framework import serializers
from .models import *
from django.contrib.auth import authenticate




class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProfileSimpleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CountrySerializers(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'

class DirectorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']




class ActorDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'

class ActorListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']



class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['genre_name']


class MovieLanguagesSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = ['language', 'video']

class MovieListSerializers(serializers.ModelSerializer):
    country = CountrySerializers(many=True)
    genre = GenreSerializers(many=True)
    avg_rating = serializers.SerializerMethodField()

    class DirectorListSerializers(serializers.ModelSerializer):
        class Meta:
            model = Director
            fields = ['director_name']

    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country','genre','movie_image', 'movie_status', 'avg_rating']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


class RatingSerializers(serializers.ModelSerializer):
      class Meta:
          model = Rating
          fields = '__all__'

class MovieMomentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = ['movie_moments']


class MovieDetailSerializer(serializers.ModelSerializer):
    country = CountrySerializers(many=True)
    genre = GenreSerializers(many=True)
    director = DirectorListSerializers(many=True)
    actor = ActorListSerializers(many=True)
    movie_languages = MovieLanguagesSerializers(many=True, read_only=True)
    movie_moments = MovieMomentsSerializers(many=True, read_only=True )
    comments = RatingSerializers(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'year', 'country','genre','director','actor','movie_image','movie_trailers','types',
                  'movie_time','description', 'movie_status','movie_languages', 'movie_moments', 'comments']







class FavoriteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class CountryDetailSerializers(serializers.ModelSerializer):
    movies = MovieListSerializers(many= True,read_only=True)
    class Meta:
        model = Country
        fields = ['country_name','movies']

class HistorySerializers(serializers.ModelSerializer):
    user = ProfileSimpleSerializers()
    movie = MovieListSerializers()

    class Meta:
        model = History
        fields =['user','movie','viewed_at']


class FavoriteMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


