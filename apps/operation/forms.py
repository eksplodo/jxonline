# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/16 10:05'
import re

from django.forms import ModelForm, ValidationError

from operation.models import UserAsk


class UserAskForm(ModelForm):
    class Meta:
        model = UserAsk
        fields = ["name", "mobile", "course"]

    def clean_mobile(self):
        """
        验证手机号是否合法
        """
        mobile = self.cleaned_data['mobile']
        pattern = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(pattern)
        if p.match(mobile):
            return mobile
        else:
            raise ValidationError("手机号码不合法！", code='mobile_invalid')