from django.urls import path

from .views import AddCategoryView, AddCommentView, AddPostView, ArticleDetailView, DeletePostView, HomeView,\
    RSSPostList, UpdatePostView, category_list_view, category_view, feedback_form, like_view


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('add_category/', AddCategoryView.as_view(), name='add_category'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:category>/', category_view, name='category'),
    path('category-list/', category_list_view, name='category-list'),
    path('like/<int:pk>', like_view, name='like_post'),
    path('article/<int:pk>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('feedback/', feedback_form, name='feedback'),
    path('rss-post/', RSSPostList.as_view(), name='rss_post_list'),

]
