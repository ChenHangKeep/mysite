from django.conf.urls import url, include

from .views import IndexView,DetailView,CategoryView,ArticleListView,MoodListView,AboutView
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^article_detail/(?P<article_id>\d+)/$', DetailView.as_view(), name="article_detail"),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name="category"),
    url(r'^article/$', ArticleListView.as_view(), name="article_list"),
    url(r'^mood_list/$', MoodListView.as_view(), name="mood_list"),
    url(r'^about/$', AboutView.as_view(), name="about"),



]
