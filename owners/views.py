import json
from django.http import JsonResponse
from django.views import View
# Create your views here.
from owners.models import Owner, Dog

class OwnersView(View):
    def post(self,request):
        data = json.loads(request.body)
        Owner.objects.create(
            name=data['name'],
            email=data['email'],
            age=data['age']
        )
        return JsonResponse({'message':'created'},status=201)
    def get(self,request):
        owners=Owner.objects.all()
        results=[]
        for owner in owners:
            results.append(
                {
                    "age":owner.age,
                    "e-mail":owner.email,
                    "name":owner.name,
                }
            )
        return JsonResponse({'results':results},status=200)

class DogsView(View):
    def post(self,request):
        data = json.loads(request.body)
        owner=Owner.objects.get(name=data['owner'])
        Dog.objects.create(
            owner = owner,
            name=data['name'],
            age=data['age'] 
        )
        return JsonResponse({'message':'created'},status=201)
    def get(self,request):
        dogs=Dog.objects.all()
        result=[]
        for dog in dogs:
            result.append(
                {
                    "name" : dog.name,
                    "age" : dog.age,
                    "owner" : dog.owner.name
                }  
            )
        return JsonResponse({'results':result},status=200)



