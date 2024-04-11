from rest_framework.decorators import action

from app01 import models
from .models import App01Book
from .models import App01Rent
from .models import App01HousePrice
from .models import App01UserInformation
from .models import App01Check

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
from .serializer import BooksSerializer
from .serializer import RentSerializer
from .serializer import HousePriceSerializer
from .serializer import UserInformationSerializer
from .serializer import CheckSerializer
# 数据库加密
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password

from django.shortcuts import render, HttpResponse

# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.middleware.csrf import get_token


def getcsrf(request):
    return JsonResponse({'csrftoken': get_token(request) or 'NOTPROVIDED'})


class CheckViewSet(viewsets.ModelViewSet):
    queryset = App01Check.objects.all()
    serializer_class = CheckSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = App01Book.objects.all()
    serializer_class = BooksSerializer


class RentViewSet(viewsets.ModelViewSet):
    queryset = App01Rent.objects.all()
    serializer_class = RentSerializer


class HousePriceViewSet(viewsets.ModelViewSet):
    queryset = App01HousePrice.objects.all()
    serializer_class = HousePriceSerializer


class UserInformationViewSet(viewsets.ModelViewSet):
    queryset = App01UserInformation.objects.all()
    serializer_class = UserInformationSerializer


def login(request):
    name = request.POST.get('name')
    password = request.POST.get('password')
    if name and password:
        try:
            user = App01UserInformation.objects.get(name=name)
        except:
            return JsonResponse({'loginstatus': 2}, safe=False)  # 未注册返回2
        if check_password(password, user.password):
            return JsonResponse({'loginstatus': 1}, safe=False)  # 登录成功返回1
    return JsonResponse({'loginstatus': 3}, safe=False)  # 密码错误返回3


def signup(request):
    name = request.POST.get("name")
    password = request.POST.get("password")
    if name and password:
        try:
            user = App01UserInformation.objects.get(name=name)
        except:
            userinfo = App01UserInformation(name=name, password=make_password(password))
            userinfo.save()  # 保存至数据库
            return JsonResponse({'codestatus': 1}, safe=False)
        return JsonResponse({'codestatus': 2}, safe=False)
