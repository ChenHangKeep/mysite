from datetime import datetime

from django.db import models

# Create your models here.

class Comment(models.Model):

    comment_name = models.CharField(max_length=20, verbose_name="名字")
    text = models.CharField(max_length=200,default="", verbose_name="评论")
    is_show = models.CharField(choices=(('show','展示'),('notshow','不展示')),default='show',verbose_name="是否展示",max_length=20)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="创建时间")

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text[:10]

# class Comments(models.Model):
#
#     comment_name = models.CharField(verbose_name='姓名', max_length=20, default='佚名')
#     text = models.CharField(verbose_name='内容', max_length=300)
#     add_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
#     class Meta:
#         verbose_name = '留言'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.text[:10]



# class Comments(models.Model):
#     """
#     留言
#     """
#     name = models.CharField(default='',max_length=30, verbose_name="评论者名字")
#     comments = models.CharField(default='',max_length=200, verbose_name="评论")
#     add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")
#
#     class Meta:
#         verbose_name = "留言"
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name
