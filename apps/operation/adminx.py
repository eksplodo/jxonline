# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/12 19:49'

import xadmin
from .models import UserAsk, CourseComment, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    display_list = ['name', 'course', 'phone', 'add_time']
    search_fields = ['name', 'course', 'phone']
    list_filter = ['name', 'course', 'phone', 'add_time']


class CourseCommentAdmin(object):
    display_list = ['user', 'comment', 'course', 'add_time']
    search_fields = ['user', 'comment', 'course']
    list_filter = ['user', 'comment', 'course', 'add_time']


class UserFavoriteAdmin(object):
    display_list = ['user', 'fav_id', 'fav_type', 'add_time']
    search_fields = ['user', 'fav_id', 'fav_type']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    display_list = ['user', 'has_read', 'message', 'add_time']
    search_fields = ['user', 'has_read', 'message']
    list_filter = ['user', 'has_read', 'message', 'add_time']


class UserCourseAdmin(object):
    display_list = ['user', 'course', 'add_time']
    search_fields = ['user', 'course']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComment, CourseCommentAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
