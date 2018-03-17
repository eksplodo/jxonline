from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg, City, Teacher

from pure_pagination import Paginator, PageNotAnInteger

class OrgListView(View):
    def get(self, request):
        page_title = "orgs"
        # 机构
        all_orgs = CourseOrg.objects.all()
        org_nums = all_orgs.count()
        # 热门排行
        hot_orgs = all_orgs.order_by("-click_nums")[:3]
        # 城市
        all_citys = City.objects.all()
        # 城市筛选
        city_id = request.GET.get('city', '')
        if city_id:
            all_orgs = all_orgs.filter(city_id=int(city_id))
            org_nums = all_orgs.count()
        # 类别筛选
        category = request.GET.get('ct', '')
        if category:
            all_orgs = all_orgs.filter(category=category)
            org_nums = all_orgs.count()
        # 排序
        sort_by = request.GET.get("sort", "")
        if sort_by:
            if sort_by == "students":
                all_orgs = all_orgs.order_by("-students")
            elif sort_by == "courses":
                all_orgs= all_orgs.order_by("-course_nums")
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, 5, request=request)
        orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_orgs': orgs,
            'all_citys': all_citys,
            'org_nums': org_nums,
            'city_id': city_id,
            'category': category,
            "hot_orgs": hot_orgs,
            "sort_by": sort_by,
            "page_title": page_title
        })


class TeacherListView(View):
    def get(self, request):
        page_title = "teachers"
        # 教师列表
        teachers = Teacher.objects.all()
        teacher_nums = teachers.count()
        # 讲师排行
        hot_teachers = teachers.order_by("-click_nums")[:3]
        # 排序
        sort_by = request.GET.get("sort", "")
        if sort_by:
            if sort_by == "hot":
                teachers = teachers.order_by("-click_nums")

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(teachers, 5, request=request)
        teachers = p.page(page)

        return render(request, 'teachers-list.html', {
            'teachers': teachers,
            'teacher_nums': teacher_nums,
            "hot_teachers": hot_teachers,
            "sort_by": sort_by,
            "page_title": page_title
        })


class OrgHomelView(View):
    def get(self, request, org_id):
        current_page = 'home'
        course_org = CourseOrg.objects.get(id=org_id)
        all_courses = course_org.course_set.all()[:3]
        all_teachers = course_org.teacher_set.all()[:2]
        return render(request, "org-detail-homepage.html", {
            "course_org": course_org,
            "all_courses": all_courses,
            "all_teachers": all_teachers,
            'current_page': current_page
        })


class OrgCourseView(View):
    def get(self, request, org_id):
        current_page = 'course'
        course_org = CourseOrg.objects.get(id=org_id)
        all_courses = course_org.course_set.all()
        return render(request, "org-detail-course.html", {
            "course_org": course_org,
            "all_courses": all_courses,
            'current_page': current_page
        })


class OrgDescView(View):
    def get(self, request, org_id):
        current_page = 'desc'
        course_org = CourseOrg.objects.get(id=org_id)
        return render(request, "org-detail-desc.html", {
            "course_org": course_org,
            'current_page': current_page
        })


class OrgTeacherView(View):
    def get(self, request, org_id):
        current_page = 'teacher'
        course_org = CourseOrg.objects.get(id=org_id)
        all_teachers = course_org.teacher_set.all()
        return render(request, "org-detail-teachers.html", {
            "course_org": course_org,
            "all_teachers": all_teachers,
            'current_page': current_page
        })


class TeacherDetailView(View):
    def get(self, request, teacher_id):
        teacher = Teacher.objects.get(id=teacher_id)
        courses = teacher.course_set.all()
        hot_teachers = teacher.org.teacher_set.order_by("-collect_nums")
        page_title = 'teachers'
        return render(request, 'teacher-detail.html', {
            "teacher": teacher,
            "courses": courses,
            "hot_teachers": hot_teachers,
            "page_title": page_title
        })