# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/15 9:38'

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from organization.views import OrgListView, UserAskView, TeacherListView, CourseView

urlpatterns = [
    path('org_list/', OrgListView.as_view(), name='org_list'),
    path('add_ask/', UserAskView.as_view(), name='add_ask'),
    path('teacher_list/', TeacherListView.as_view(), name="teacher_list"),
    path('course_list', CourseView.as_view(), name='course_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # 配置上传文件的处理地址