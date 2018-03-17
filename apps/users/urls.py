# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/13 10:34'


from django.urls import path
from django.views.generic import TemplateView
from .views import LoginView, RegisterView, ActiveView,\
    ForgetView, PwdResetView, UpdatePwdView, LogoutView, IndexView

app_name = "users"
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('active/<str:active_code>/', ActiveView.as_view(), name='avtive'),
    path('forget/', ForgetView.as_view(), name='forget'),
    path('forget/<str:forget_code>', PwdResetView.as_view(), name='reset_pwd'),
    path('updatepwd/', UpdatePwdView.as_view(), name='update_pwd'),
    path('logout/', LogoutView.as_view(), name='logout')
]