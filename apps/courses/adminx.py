# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/12 17:38'

import xadmin

from .models import Course, Lession, Video, CourseResource


class CourseAdmin(object):
    list_display = ['name', 'desc', 'degree', 'learn_times', 'students', 'collect_nums', 'click_nums', 'add_time']
    search_fields = ['name', 'desc', 'degree', 'learn_times', 'students', 'collect_nums', 'click_nums']
    list_filter = ['name', 'desc', 'degree', 'learn_times', 'students', 'collect_nums', 'add_time', 'click_nums']


class LessionAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['name', 'lession', 'add_time']
    search_fields = ['name', 'lession']
    list_filter = ['name', 'add_time', 'lession__name']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'download', 'add_time']
    search_fields = ['name', 'course', 'download']
    list_filter = ['name', 'add_time', 'course__name', 'download']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lession, LessionAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
