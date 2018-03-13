# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/12 16:35'

import xadmin
from xadmin.views import BaseAdminView, CommAdminView

from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = '不学后台管理系统'
    site_footer = '不学在线教育'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'add_time', 'url']
    search_fields = ['title', 'image']
    list_filter = ['title', 'image', 'add_time', 'url']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(BaseAdminView, BaseSetting)
xadmin.site.register(CommAdminView, GlobalSetting)
