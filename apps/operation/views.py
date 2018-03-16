from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import UserAsk
from .forms import UserAskForm


class UserAskView(View):
    """
    用户咨询表单提交
    """
    def post(self, request):
        ask_form = UserAskForm(request.POST)
        if UserAskForm.is_valid:
            user_ask = ask_form.save()
            return HttpResponse("{'status': 'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status': 'fail','msg': '提交出错'}", content_type='application/json')

