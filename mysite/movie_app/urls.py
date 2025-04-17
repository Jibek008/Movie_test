
from rest_framework import routers
from .views import *
from django.urls import path,include

router = routers.SimpleRouter()
router.register(r'directors',DirectorViews,basename='Director_list')
router.register(r'genre',GenreViews,basename='Genre_list')
router.register(r'rating',RatingViews,basename='Rating_list')
router.register(r'favorite',FavoriteViews,basename='Favorite_list')
router.register(r'history',HistoryViews,basename='History_list')
router.register(r'country',CountryViews,basename='Country_List')

urlpatterns = [
    path('',include(router.urls)),
    path('movie/',MovieListAPIView.as_view(),name='movie_list'),
    path('movie/<int:pk>/',MovieDetailAPIView.as_view(),name = 'movie_detail'),
    path('users/',ProfileListAPIView.as_view(),name='user_list'),
    path('user/<int:pk>/',ProfileEditAPIView.as_view(),name='user_detail'),
    path('actor/',ActorLIstAPIVew.as_view(),name = 'actor_list'),


]