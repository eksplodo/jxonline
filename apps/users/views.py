from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password

from .forms import LoginForm, RegisterForm, ForgetForm, PwdUpdateForm
from .models import UserProfile, EmailVerifyRecord
from utils import send_verify_email


class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception:
            return None


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html', {'username': user_name})
                else:
                    return render(request, 'register.html', {})
            else:
                return render(request, 'login.html', {'msg': '用户名或密码错误！！！', 'login_form': login_form})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class ActiveView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                return render(request, 'login.html')
        else:
            return render(request, 'active_fail.html')



class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'register.html', {'register_form': register_form, 'msg': '用户已存在'})
            else:
                userprofile = UserProfile()
                pass_word = request.POST.get('password', '')
                userprofile.username = user_name
                userprofile.email = user_name
                userprofile.password = make_password(pass_word)
                userprofile.is_active = False
                userprofile.save()

                send_verify_email(user_name, 'register')
                return render(request, 'send_sucess.html')
        else:
            return render(request, 'register.html', {'register_form': register_form})


class ForgetView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_verify_email(email, 'forget')
            return render(request, 'send_sucess.html')
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class PwdResetView(View):
    def get(self, request, forget_code):
        all_records = EmailVerifyRecord.objects.filter(code=forget_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'active_fail.html')


class UpdatePwdView(View):
    def post(self, request):
        pwdupdate_form = PwdUpdateForm(request.POST)
        if pwdupdate_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 == pwd2:
                user = UserProfile.objects.get(email=email)
                user.password = make_password(pwd2)
                user.save()
                return render(request, 'login.html')
            else:
                return render(request, 'password_reset.html', {'msg': '两次密码输入不同！请检查并重新输入。'})
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'email': email, 'pwdupdate_form': pwdupdate_form})
