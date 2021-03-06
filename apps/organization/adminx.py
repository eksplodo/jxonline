# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/12 19:30'

import xadmin
from .models import City, CourseOrg, Teacher


class CityAdmin(object):
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    list_display = ['name', 'address', 'city', 'category', 'course_nums', 'desc', 'click_nums', 'collect_nums', 'add_time']
    search_fields = ['course_nums', 'desc', 'click_nums', 'collect_nums', 'address', 'city']
    list_filter = ['course_nums', 'desc', 'click_nums', 'collect_nums', 'address', 'city', 'add_time']


class TeacherAdmin(object):
    list_display = ['name', 'org', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'collect_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'collect_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'collect_nums', 'add_time']


xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)