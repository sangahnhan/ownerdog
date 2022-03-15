from django.urls import path
from movies.views import *

urlpatterns = [
    path('actor',ActorsView.as_view()),
    path('movie',MoviesView.as_view()),
    path('actormovie',ActorMovieView.as_view())
]
