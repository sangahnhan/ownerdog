
from django.urls import path, include
from manytomany.views import *
urlpatterns = [
    path('actor',ActorView.as_view()),
    path('movie',MovieView.as_view()),
]
