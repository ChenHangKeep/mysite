from django.shortcuts import render
from django.views.generic.base import View
from django.db.models.aggregates import Count
from django.http import HttpResponse

from pure_pagination import Paginator, PageNotAnInteger
from blog.models import Article, Category
from .models import Comment
from .forms import CommentForm

# Create your views here.

class CommentView(View):
    def get(self, request):
        article_num = Article.objects.count()  # 统计文章数量
        comment_num = Comment.objects.count()  # 统计评论数量
        read_article = Article.objects.all().order_by("read_num")[:10]  # 点击排行

        #   热门分类
        #  Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
        hot_category = Category.objects.annotate(num_articles=Count('article')).order_by('-num_articles')[:8]
        newest_article = Article.objects.all().order_by("-add_time")[:10]  # 最新发布

        #取出所有评论
        all_comment = Comment.objects.filter(is_show='show').order_by('-add_time')
        #对评论进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_comment, 10, request=request)
        comments = p.page(page)

        return render(request, 'comment.html',{
            'hot_category': hot_category,
            'newest_article': newest_article,
            'read_article': read_article,
            'article_num': article_num,
            'comment_num': comment_num,
            'all_comment': comments
        })


class AddCommentView(View):

    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail"}', content_type='application/json')

