# -*- coding: utf-8 -*-

__author__ = 'gbc'
__date__ = '2018/3/14 8:38'

import string
from random import Random

from django.core.mail import send_mail
from jxonline.settings import EMAIL_FROM

from users.models import EmailVerifyRecord


def send_verify_email(email, send_type='register'):
    emailverifyrecord = EmailVerifyRecord()
    code = random_code(16)
    emailverifyrecord.email = email
    emailverifyrecord.send_type = send_type
    emailverifyrecord.code = code
    emailverifyrecord.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '不学在线注册邮件'
        email_body = '欢迎注册不学在线，请点击以下链接进行激活：http://127.0.0.1:8000/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = '不学在线密码找回'
        email_body = '这是一封密码找回邮件，如果不是本人操作，请忽略它，如果是本人操作，请点击下面链接已重置密码：http://127.0.0.1:8000/forget/{0}'.format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def random_code(length=8):
    code = ''
    chars = string.ascii_letters + string.digits
    nums = len(chars) - 1
    random = Random()
    for i in range(length):
        code += chars[random.randint(0, nums)]
    return code
