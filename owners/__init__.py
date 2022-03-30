View.py
import json
import re # 이메일 매칭 확인

from django.http import JsonResponse
from django.views import View
from users.models import *
#from django.shortcuts import render

# 회원가입시 서로 다른 사람이 같은 이메일 사용하지 않으므로
# 기존에 존재하는 자료와 중복되면 안됨. 적절한 에러 반환

# 회원가입이 성공하면 {"message": "SUCCESS"}, status code 201 반환

class UserSignInView(View):
    # 이메일 @ . 필수 포함
    EMAIL_FORMAT = '[^@]+@[^@]+\.[^@]+'
    # 비밀번호 8자리 이상, 문자, 숫자, 특수문자 복합
    PASSWORD_FORMAT = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,20}$"
    def post(self,resquest):
        try:
            # name, email, password, phonenumber, 그 외 정보 포함
            user_data = json.loads(request.body)
            # 이메일 포맷 확인
            if not re.match(EMAIL_FORMAT, user_data['email']): 
                return JsonResponse({'message':'EMAIL_FORMAT_ERROR'},status=400)
            # 비밀번호 포맷 확인
            if not re.match(PASSWORD_FORMAT,user_data['password']): 
                return JsonResponse({'message':'PASSWORD_FORMAT_ERROR'},status=400)
            # 중복 이메일 확인
            if not User.objects.filter(email = user_data['email'])==[]:
                return JsonResponse({'message':'EMAIL_OVERLAP_ERROR'},status=400)
            return JsonResponse({"message": "SUCCESS"}, status=201)
        except KeyError: 
            return JsonResponse({'message':'KEY_ERROR'},status=400)

class UserSignUpView(View):
    def post(self,request):
        try:
            user_data = json.loads(request.body)
            User.objects.create(
                name=user_data['name'],
                email=user_data['email'],
                password=user_data['password'],
                phonenumber=user_data['phonenumber']
            )
            JsonResponse({'message':'created'},status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'},status=400)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'},status=400)
