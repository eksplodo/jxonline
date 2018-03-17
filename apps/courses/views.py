import random

from django.shortcuts import render

from django.views.generic import View
from .models import Course, Video, Lession, CourseResource


class CourseView(View):
    def get(self, request):
        page_title = "courses"
        return render(request, 'course-list.html', {
            "page_title": page_title
        })

class CourseDetailView(View):
    def get(self, request, course_id):
        page_title = 'courses'
        course = Course.objects.get(id=course_id)
        lessions = course.lession_set.count()
        teachers = course.course_org.teacher_set.count()
        return render(request, 'course-detail.html', {
            "course": course,
            "page_title": page_title,
            "lessions": lessions,
            "teachers": teachers,
        })


class CourseVideoView(View):
    def get(self, request, course_id):
        page_title = 'courses'
        course = Course.objects.get(id=course_id)
        lessions = [lession_id for lession_id in Lession.objects.filter(course_id=course_id)]
        course_resources = CourseResource.objects.filter(course=course)
        return render(request, 'course-video.html', {
            "pge_title": page_title,
            "lessions": lessions,
            "course": course,
            "course_resources": course_resources,
        })
