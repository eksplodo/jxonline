# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/15 9:38'

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from organization.views import \
    OrgListView, TeacherListView,\
    OrgHomelView, OrgCourseView,\
    OrgDescView, OrgTeacherView,\
    TeacherDetailView

app_name = "organization"
urlpatterns = [
    path('org/list/', OrgListView.as_view(), name='org_list'),
    # 授课老师
    path('teachers/', TeacherListView.as_view(), name="teacher_list"),
    path('teacher/detail/<int:teacher_id>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('home/<int:org_id>/', OrgHomelView.as_view(), name='org_home'),
    path('home/<int:org_id>/courses/', OrgCourseView.as_view(), name='org_courses'),
    path('home/<int:org_id>/desc/', OrgDescView.as_view(), name='org_desc'),
    path('home/<int:org_id>/teacher/', OrgTeacherView.as_view(), name='org_teacher'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   # 配置上传文件的处理地址