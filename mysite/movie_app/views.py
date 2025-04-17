from rest_framework import viewsets,generics
from.serializers import *
from .models import *
from .permissions import CheckStatus,CheckUserRating

class ProfileListAPIView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers


    def get_queryset(self):
        return Profile.objects.filter(id =self.request.user.id)

class ProfileEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializers


    def get_queryset(self):
        return Profile.objects.filter(id =self.request.user.id)



class CountryViews(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers


class ActorLIstAPIVew(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializers


class ActorDetailAPIView(generics.RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializers


class DirectorViews(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializers


class GenreViews(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers


class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializers

class MovieDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieDetailSerializer
    permission_classes = [CheckStatus]



class RatingViews(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    permission_classes = [CheckUserRating]


class FavoriteViews(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializers



class CountryDetailViewSet(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers


class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializers


class HistoryViews(viewsets.ModelViewSet):
    queryset = History.objects.all()
    serializer_class = HistorySerializers




class FavoriteItemViews(viewsets.ModelViewSet):
    queryset = FavoriteMovie.objects.all()
    serializer_class = FavoriteSerializers


def  get_queryset(self):
    return History.objects.filter(user=self.request.user)






































