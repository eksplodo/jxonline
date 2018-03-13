from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name='昵称', default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(choices=(('male', '男'), ('female', '女')), default='female', max_length=10,
                              verbose_name='性别')
    address = models.CharField(max_length=500, default='', verbose_name='联系地址')
    mobile = models.CharField(max_length=11, null=True, blank=True, verbose_name='手机号')
    image = models.ImageField(upload_to='image/%Y%m', default='image/default.png', max_length=100, verbose_name='头像')

    class Meta:
        verbose_name = '用户基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_type = models.CharField(max_length=10, choices=(('register', '注册'), ('forget', '找回密码')),
                                 default='register', verbose_name='类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}{1}'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y%m', verbose_name='轮播图', max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
