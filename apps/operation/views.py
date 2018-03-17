from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from .models import UserFavorite
from courses.models import Course
from organization.models import CourseOrg, Teacher
from .forms import UserAskForm


class UserAskView(View):
    """
    用户咨询表单提交
    """
    def post(self, request):
        ask_form = UserAskForm(request.POST)
        if ask_form.is_valid:
            user_ask = ask_form.save(commit=True)
            return HttpResponse("{'status': 'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status': 'fail','msg': '提交出错'}", content_type='application/json')


class UserFavView(View):
    """
    用户收藏和取消收藏
    """
    def post(self, request):
        fav_id = request.POST.get('fav_id', 0)
        fav_type = request.POST.get('fav_type', 0)
        if not request.user.is_authenticated():
            return HttpResponse("{'status': 'fail', 'msg': '用户未登录'}", content_type='application/json')
        exist_records = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
        if exist_records:
            # 已经收藏了, 删除收藏
            exist_records.delete()
            if int(fav_type) == 1:
                course = Course.objects.get(id=int(fav_id))
                course.collect_nums -= 1
                if course.collect_nums < 0:
                    course.collect_nums = 0
                    course.save()
            elif int(fav_type) == 2:
                org = CourseOrg.objects.get(id=int(fav_id))
                org.collect_nums -= 1
                if org.collect_nums < 0:
                    org.collect_nums = 0
                    org.save()
            elif int(fav_type) == 3:
                teacher = Teacher.objects.get(id=int(fav_id))
                teacher.collect_nums -= 1
                if teacher.collect_nums < 0:
                    teacher.collect_nums = 0
                    teacher.save()
        else:
            # 未收藏，收藏
            user_fav = UserFavorite()
            if int(fav_id) > 0 and int(fav_type) > 0:
                user_fav.fav_id = int(fav_id)
                user_fav.fav_type = int(fav_type)
                user_fav.user = request.user
                user_fav.save()
                if int(fav_type) == 1:
                    course = Course.objects.get(id=int(fav_id))
                    course.collect_nums += 1
                    course.save()
                elif int(fav_type) == 2:
                    org = CourseOrg.objects.get(id=int(fav_id))
                    org.collect_nums += 1
                    org.save()
                elif int(fav_type) == 3:
                    teacher = Teacher.objects.get(id=int(fav_id))
                    teacher.collect_nums += 1
                    teacher.save()
                return HttpResponse("{'status': 'success', 'msg': '已收藏'}", content_type='application/json')
            return HttpResponse("{'status': 'fail', 'msg': '收藏出错'}", content_type='application/json')


