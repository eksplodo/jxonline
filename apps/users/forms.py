# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/13 14:47'

from django import forms

from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    # phone = forms.CharField(required=True, max_length=11)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={'invaild': '验证码错误！'})
