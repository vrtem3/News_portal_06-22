from django.urls import path
from .views import PostList, PostDetail, PostCreateNews, PostCreateArticles, PostEdit, PostDelete


urlpatterns = [
    path('', PostList.as_view(), name='post_list'), 
    path('<int:post_id>', PostDetail.as_view(), name='post_detail'),
    path('news/create/', PostCreateNews.as_view(), name='post_nw_create'),
    path('news/<int:pk>/edit/', PostEdit.as_view(), name='post_nw_edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_nw_delete'),
    path('articles/create/', PostCreateArticles.as_view(), name='post_ar_create'),
    path('articles/<int:pk>/edit/', PostEdit.as_view(), name='post_ar_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='post_ar_delete'),
    path('search/', PostList.as_view(), name='post_search'),
]