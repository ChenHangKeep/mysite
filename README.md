# 基于Djano的个人博客
## 项目介绍
* 一个基于Python+Django框架的个人博客网站，使用nginx_uwsgi部署到本地服务器；

## 项目环境
  * Python3.6
  * Django1.11
  * 第三方库：pip install requirements.txt
  * nginx+uwsgi

## 相关功能：
  * admin管理 换成 xadmin，支持富文本编辑；
  * 文章标签类别自定义，文章管理；
  * 文章展示，按照文章标签分类展示，分页展示，文章详情阅读，展示文章和图片详情；
  * 搜索文章。全文搜索功能，列出匹配的文章列表；
  * 留言功能；
  
  # 注意事项
  * 因为上传的项目是部署过之后的，所以静态文件加载方式不一样
   * 在开发环境下：</br>
   >>在urls.py注释掉下面两行:</br>
   ```Python
    #   url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    #   url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
   ```
   并在Settings中添加：
   ```Python
    STATIC_URL = '/static/'
    #  STATIC_ROOT = 'static'
    STATICFILES_DIRS = [
         os.path.join(BASE_DIR, 'static'), ##修改地方
      ]
   ```
  # 最后
  >>> * 在写本项目是的时候，感觉最重要的还是整体的规划和设计思路，这两点如果能想好，可以避免后续的很多不必要的麻烦，流程也会清晰很多。</br>
  >>> * 收获最大的还是学习到了遇到问题时解决问题的思路；</br>  
  >>> * 这个项目我会持续更新,像登录注册，文章评论，还有其他的一些功能我都会慢慢完善;
