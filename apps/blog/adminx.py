import xadmin
from xadmin import views

from .models import Article, Banner, Category, Notice
from comments.models import Comment

#将对应的model注册到xamdin后台


class BaseSetting(object):
    """
    全局主题设置
    """
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    """
    页头，页脚，左边菜单栏
    """
    site_title = "网站后台管理系统"
    site_footer = "陈航个人网站"
    menu_style = "accordion"


class ArticleAdmin(object):
    """
    文章显示，搜索，排序，只读字段
    """
    list_display = ['title', 'author', 'brief', 'is_top', 'read_num', 'add_time']
    list_editable = ['is_top']
    style_fields = {'body': 'ueditor'}
    search_fields = ['title', 'author', 'brief', 'add_time']
    ordering = ['add_time']
    #readonly_fields = ['read_num']


class BannerAdmin(object):
    """
    轮播图相关信息
    """
    list_display = ['title', 'url', 'add_time']


class CommentsAdmin(object):
    """
    留言
    """
    list_display = ['comment_name','text', 'add_time','is_show']
    list_editable = ['is_show']


class CategoryAdmin(object):
    list_display = ['category_name', 'add_time']


class NoticeAdmin(object):
    list_display = ['title', 'content','is_show', 'add_time']
    list_editable = ['is_show']


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Notice, NoticeAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(Comment, CommentsAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)

