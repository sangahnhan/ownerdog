import json
from django.http import JsonResponse
from django.views import View
from movies.models import *
# Create your views here.

class ActorsView(View):
    def post(self,request): 
        # first_name, last_name, date_of_birth
        data = json.loads(request.body)
        Actor.objects.create(
            first_name    = data['first_name'],
            last_name     = data['last_name'],
            date_of_birth = data['date_of_birth']
        )
        return JsonResponse({'message':"created"},status=201)
    def get(self,request):
        datas   = Actor.objects.all()
        # results = []
        # for data in datas: 
        #     movie_list = []
        #     movies     = data.actor_movie_set.all()
        #     for movie in movies: 
        #         movie_list.append(
        #             {
        #                 "movie": movie.movie.title
        #             }
        #         )
        #     results.append(
        #         {
        #             "first_name"   : data.first_name,
        #             "last_name"    : data.last_name,
        #             "date_of_birth": data.date_of_birth,
        #             "movie_list"   : movie_list
        #         }
        #     )
        
        results = [{
                    "first_name"   : data.first_name,
                    "last_name"    : data.last_name,
                    "date_of_birth": data.date_of_birth,
                    "movie_list"   : [{"movie" : actormovie.movie.title} for actormovie in data.actor_movie_set.all()]
                } for data in datas]
        return JsonResponse({'results':results},status=200)
class MoviesView(View):
    def post(self,request): 
        data = json.loads(request.body)
        Movie.objects.create(
            title        = data['title'],
            release_date = data['release_date'],
            running_time = data['running_time']
        )
        # Actors.objects.get(data['last_name']).movies.add(Movies.objects.get(data=[title]))
        return JsonResponse({"message":"created"},status=201)
    def get(self,request): 
        datas   = Movie.objects.all()
        results = []
        for data in datas: 
            results.append(
                {
                    "title"       : data.title,
                    "release_date": data.release_date,
                    "running_time": data.running_time
                }
            )
        return JsonResponse({"results":results},status=200)
class ActorMovieView(View):
    def post(self,request): 
        data  = json.loads(request.body)
        actor = Actor.objects.get(id=data['actor_id'])
        movie = Movie.objects.get(id=data['movie_id'])
        Actor_Movie.objects.create(
            actor = actor,
            movie = movie
        )
        return JsonResponse({'message':'created'},status=201)
    def get(self,request): 
        datas   = Actor_Movie.objects.all()
        results = []
        for data in datas: 
            results.append(
                {
                    "actor_id": data.actor.id,
                    "movie_id": data.movie.id
                }
            )
        return JsonResponse({'results':results},status=200)