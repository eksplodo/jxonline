from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from courses.views import CourseView, CourseDetailView, CourseVideoView

app_name = "courses"
urlpatterns = [
    path('', CourseView.as_view(), name='course_list'),
    path('detail/<int:course_id>', CourseDetailView.as_view(), name='course_detail'),
    path('detail/<int:course_id>/video/', CourseVideoView.as_view(), name='course_video'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)