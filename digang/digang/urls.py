"""digang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.urls import re_path as url
from django.views.generic import TemplateView
from app01 import views

urlpatterns = (
    path('admin/', admin.site.urls),
    # path('index/', views.index),
    # 让访问api/路径时候转到app01应用中的urls.py文件配置进行处理
    path('api/', include('app01.urls')),
    # 前端文件
    path('', TemplateView.as_view(template_name='index.html')),
    path('regster/', views.signup),
    path('login/', views.login),
    path('getcsrf/', views.getcsrf),
)
