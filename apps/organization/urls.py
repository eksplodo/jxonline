# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/15 9:38'

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from organization.views import \
    OrgListView, TeacherListView, CourseView, \
    OrgHomelView, OrgCourseView, OrgDescView, OrgTeacherView

app_name = "organization"
urlpatterns = [
    path('list/', OrgListView.as_view(), name='org_list'),
    path('teacher_list/', TeacherListView.as_view(), name="teacher_list"),
    path('course_list', CourseView.as_view(), name='course_list'),
    path('home/<int:org_id>/', OrgHomelView.as_view(), name='org_home'),
    path('home/<int:org_id>/courses/', OrgCourseView.as_view(), name='org_courses'),
    path('home/<int:org_id>/desc/', OrgDescView.as_view(), name='org_desc'),
    path('home/<int:org_id>/teacher/', OrgTeacherView.as_view(), name='org_teacher'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # 配置上传文件的处理地址