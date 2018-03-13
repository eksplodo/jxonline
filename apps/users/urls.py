# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/13 10:34'


from django.urls import path, include
from django.views.generic import TemplateView
from .views import LoginView, RegisterView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register', RegisterView.as_view(), name='register'),
    path('captcha', include('captcha.urls')),
]