from django.shortcuts import render, HttpResponse
from django.views.generic import View
from .models import CourseOrg, City, Teacher
from .forms import UserAskForm

from pure_pagination import Paginator, PageNotAnInteger

class OrgListView(View):
    def get(self, request):
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
        })


class UserAskView(View):
    """
    用户咨询表单提交
    """
    def post(self, request):
        ask_form = UserAskForm(request.POST)
        if UserAskForm.is_valid:
            user_ask = ask_form.save()
            return HttpResponse("{'status': 'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status': 'fail','msg': '提交出错'}", content_type='application/json')

class TeacherListView(View):
    def get(self, request):
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
        })


class CourseView(View):
    def get(self, request):
        return render(request, 'course-list.html', {})


class OrgDetailView(View):
    def get(self, request):
        pass