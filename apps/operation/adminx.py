# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/12 19:49'

import xadmin
from .models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    display_list = ['name', 'course', 'monile', 'add_time']
    search_fields = ['name', 'course', 'mobile']
    list_filter = ['name', 'course', 'mobile', 'add_time']


class CourseCommentAdmin(object):
    display_list = ['user', 'comment', 'course', 'add_time']
    search_fields = ['user', 'comment', 'course']
    list_filter = ['user', 'comment', 'course', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'has_read', 'message', 'add_time']
    search_fields = ['user', 'has_read', 'message']
    list_filter = ['user', 'has_read', 'message', 'add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
