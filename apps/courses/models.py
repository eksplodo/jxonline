from datetime import datetime

from django.db import models
from organization.models import CourseOrg, Teacher

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='课程名称')
    desc = models.CharField(max_length=300, verbose_name='描述')
    detail = models.TextField(verbose_name='课程详情')
    degree = models.CharField(choices=(('初级', 'cj'), ('终极', 'zj'), ('高级', 'gj')), max_length=2, verbose_name='等级')
    learn_times = models.IntegerField(default=0, verbose_name='课程时长（分钟数）')
    students = models.IntegerField(default=0, verbose_name='学习人数')
    collect_nums = models.IntegerField(default=0, verbose_name='收藏人数')
    image = models.ImageField(upload_to='courses/%Y%m', max_length=100, verbose_name='课程刊图', null=True, blank=True)
    click_nums = models.IntegerField(default=0, verbose_name='点击量')
    # 课程授课老师
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='授课老师', null=True, blank=True)
    # 添加课程所属机构
    course_org = models.ForeignKey(CourseOrg, on_delete=models.CASCADE, null=True, blank=True, verbose_name="课程机构")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Lession(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    name = models.CharField(max_length=100, verbose_name='章节名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Video(models.Model):
    name = models.CharField(max_length=100, verbose_name='章节名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    lession = models.ForeignKey(Lession, on_delete=models.CASCADE, verbose_name='章节')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    name = models.CharField(max_length=100, verbose_name='资源名称')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='课程')
    download = models.FileField(upload_to='courses/resource/%Y%m', verbose_name='资源文件', max_length='100')

    class Meta:
        verbose_name = '课程资源'
        verbose_name_plural = verbose_name
