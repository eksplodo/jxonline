from django.shortcuts import render, HttpResponse
from django.views import View
# from django.http import HttpResponse

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

        if not request.user.is_authenticated:
            # 判断用户是否登陆
            return HttpResponse("{'status': 'fail', 'msg': '用户未登录'}", content_type="application/json")
        else:
            # 查询是否存在记录，存在者删除，否则添加
            record = UserFavorite.objects.filter(user=request.user, fav_id=int(fav_id), fav_type=int(fav_type))
            if record:
                record.delete()
                return HttpResponse("{'status': 'success', 'msg': '收藏'}", content_type="application/json")
            else:
                # 判断fav_id和fav_type的值，如果都等于零，则返回收藏出错。
                if int(fav_id) > 0 and int(fav_type) > 0:
                    user_fav = UserFavorite()
                    user_fav.fav_id = int(fav_id)
                    user_fav.fav_type = int(fav_type)
                    user_fav.user = request.user
                    user_fav.save()
                    return HttpResponse("{'status': 'success', 'msg': '已收藏'}", content_type="application/json")
                else:
                    return HttpResponse("{'status': 'fail', 'msg': '收藏失败'}", content_type="application/json")



