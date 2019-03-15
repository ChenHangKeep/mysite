from datetime import datetime
from DjangoUeditor.models import UEditorField

from django.db import models


# Create your models here.
#根据前端页面设计需求


class Article(models.Model):
    """
    标题，标签，作者，简介，阅读数，body支持富文本(前端设置{% autoescape off %}阻止字符转义)，发布时间
    """

    category = models.ForeignKey('Category',default='', on_delete=models.CASCADE, verbose_name="文章类别")
    title = models.CharField(default='', max_length=200, verbose_name="标题")
    author = models.CharField(default='', max_length=50, verbose_name="作者")
    brief = models.TextField(default='', max_length=150, verbose_name="简介")
    body = UEditorField(width=700, height=300, toolbars="full", imagePath="images/",
                        filePath="files/",upload_settings={"imageMaxSize":1204000},settings={}, verbose_name='内容')
    read_num = models.IntegerField(default=0, verbose_name="阅读数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="发布时间")
    is_top = models.BooleanField(default=False, verbose_name="是否置顶") #

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Banner(models.Model):
    """
    轮播图
    """
    title = models.CharField(max_length=100, verbose_name="标题")
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name="轮播图", max_length=100)
    url = models.URLField(max_length=200, verbose_name="访问地址")
    index = models.IntegerField(default=100, verbose_name="顺序")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name



class Category(models.Model):
    category_name = models.CharField(default="", max_length=20,verbose_name="文章类别")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "文章类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


#公告
class Notice(models.Model):
    title = models.CharField(default='', max_length=30,verbose_name="公告标题")
    content = models.TextField(default='', verbose_name="公告内容")
    is_show = models.BooleanField(default=False, verbose_name="是否显示")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "站点公告"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
