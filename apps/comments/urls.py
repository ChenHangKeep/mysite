from django.conf.urls import url, include

from .views import *
urlpatterns = [
    url(r'^comments/$', CommentView.as_view(), name="comment"),
    # url(r'^add_commnent/$', AddCommentView.as_view(), name="add_comment"),
    url(r'^add_comment/$',AddCommentView.as_view(), name='add_comment'),
]