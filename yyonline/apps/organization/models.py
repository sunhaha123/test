# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from  datetime import datetime
from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"城市名称")
    add_time = models.DateTimeField(default=datetime.now)
    desc = models.CharField(verbose_name=u"城市描述",max_length=200)

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class CourseOrg(models.Model):
    name = models.CharField(max_length=50,verbose_name=u"机构名称")
    desc = models.TextField(verbose_name=u"机构描述")
    tag = models.CharField(max_length=10,verbose_name=u"机构标签",default="全国知名")
    catgory = models.CharField(max_length=20,choices=(("pxjg","培训就够"),("gx","高校"),("gr","个人")),verbose_name="机构类别",default="gx")
    click_nums = models.IntegerField(default=0,verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    image = models.ImageField(upload_to="org/%Y/%m", verbose_name="logo", max_length=100)
    address = models.CharField(max_length=150,verbose_name=u"机构地址")
    city = models.ForeignKey(CityDict,verbose_name=u"所在城市")
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = u"模型列表"
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        #获取课程机构教师的数量
        return  self.teacher_set.all().count()

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=20, verbose_name=u"名")
    work_years = models.IntegerField(default=0,verbose_name=u"工作年限")
    work_company = models.CharField(max_length=50,verbose_name=u"就职名称")
    work_position = models.CharField(max_length=50, verbose_name=u"公司职位")
    points = models.CharField(max_length=50, verbose_name=u"教学特点")
    image = models.ImageField(max_length=100, upload_to='teacher/%Y%m', verbose_name=u"头像", default="")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    add_time = models.DateTimeField(default=datetime.now)
    org = models.ForeignKey(CourseOrg ,verbose_name=u"所属机构")
    age = models.IntegerField(default=18,verbose_name=u"年龄")

    class Meta:
        verbose_name = u"教练"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name