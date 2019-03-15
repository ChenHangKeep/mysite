from django.shortcuts import render
from django.views.generic.base import View
from django.db.models.aggregates import Count
from django.http import HttpResponse
from django.db.models import Q
from django.shortcuts import render_to_response

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Article, Notice, Category, Banner
from comments.models import Comment


# Create your views here.


class IndexView(View):
    def get(self,request):
        all_article = Article.objects.all().order_by("-add_time")#取出所有文章
        article_num = Article.objects.count()#统计文章数量
        comment_num = Comment.objects.count()#统计评论数量
        top_article = Article.objects.get(is_top=True)#置顶文章
        all_notice = Notice.objects.get(is_show=True)#站点公告

        #热门分类  Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
        hot_category = Category.objects.annotate(num_articles=Count('article')).order_by('-num_articles')[:8]
        read_article = Article.objects.all().order_by("read_num")[:10]#   点击排行

        all_banner = Banner.objects.all()

        #文章搜索功能
        search_keywords = request.GET.get('q', '')
        if search_keywords:
            all_article = all_article.filter(
                Q(title__icontains=search_keywords))

        #对文章进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_article, 5, request=request)
        articles = p.page(page)
        return render(request, 'index.html', {
            'all_article': articles,
            'top_article': top_article,
            'all_notice': all_notice,
            'hot_category': hot_category,
            'read_article': read_article,
            'article_num':article_num,
            'comment_num':comment_num,
            'all_banner':all_banner
           })


class ArticleListView(View):
    def get(self, request):
        all_article = Article.objects.all().order_by("-add_time")#取出所有文章
        newest_article = Article.objects.all().order_by("-add_time")[:10]#最新发布
        read_article = Article.objects.all().order_by("read_num")[:10]#   点击排行
        # 热门分类  Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
        hot_category = Category.objects.annotate(num_articles=Count('article')).order_by('-num_articles')[:8]

        #文章搜索功能
        search_keywords = request.GET.get('q', '')
        if search_keywords:
            all_article = all_article.filter(
                Q(title__icontains=search_keywords))

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_article, 10, request=request)
        articles = p.page(page)

        return render(request,'article.html',{
            "read_article": read_article,
            "newest_article": newest_article,
            'all_article': articles,
            'hot_category':hot_category
        })


class DetailView(View):
    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))#取出对应文章
        article_num = Article.objects.count()#统计文章数量
        comment_num = Comment.objects.count()#统计评论数量
        read_article = Article.objects.all().order_by("read_num")[:10]#   点击排行

        #   热门分类
        #  Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
        hot_category = Category.objects.annotate(num_articles=Count('article')).order_by('-num_articles')[:8]
        newest_article = Article.objects.all().order_by("-add_time")[:10]#   最新发布

        return render(request, 'article_detail.html', {
            'article': article,
            'hot_category': hot_category,
            'newest_article': newest_article,
            'read_article':read_article,
            'article_num': article_num,
            'comment_num': comment_num
        })


class CategoryView(View):
    def get(self, request, category_id):
        cate_article = Article.objects.filter(category_id=category_id)

        all_notice = Notice.objects.get(is_show=True)  # 站点公告

        cate = Category.objects.get(id=int(category_id))

        # 热门分类  Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
        hot_category = Category.objects.annotate(num_articles=Count('article')).order_by('-num_articles')[:8]
        read_article = Article.objects.all().order_by("read_num")[:10]  # 点击排行

        # 对文章进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(cate_article, 10, request=request)
        articles = p.page(page)


        return render(request, 'category.html',{
            "cate_article": articles,
            'all_notice': all_notice,
            'hot_category': hot_category,
            'read_article': read_article,
            'cate':cate
        })


class MoodListView(View):
    def get(self, request):
        all_article = Article.objects.all().order_by("-add_time")

        # 对文章进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_article, 30, request=request)
        articles = p.page(page)
        return render(request, 'moodList.html',{
            'all_article':articles
        })


class AboutView(View):
    def get(self, request):
        return render(request,'about.html',{

        })


def page_not_found(request):
    return render_to_response('404.html')

def page_error(request):
    return render_to_response('404.html')