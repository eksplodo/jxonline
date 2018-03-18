# -*- coding: utf-8 -*-
__author__ = 'gbc'
__date__ = '2018/3/16 10:03'
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import UserAskView, UserFavView

app_name = "operation"
urlpatterns = [
    path('ask/', UserAskView.as_view(), name='add_ask'),
    path('favorite/', UserFavView.as_view(), name='add_fav')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)