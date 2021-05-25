from django.urls import path, re_path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.PostList.as_view(), name = 'home'),
    path('post/<int:pk>/', views.PostRead.as_view(), name = 'postRead'),
    path('<int:pk>/comment', views.add_comment, name='add_comment'),
    path('<int:pk>/comment', views.comment_remove, name='comment_remove'),
    path('post/new/', views.post_new, name='postNew'),
    path('post/<int:pk>/', views.post_remove,  name='postDelete'),
    path('post/edit/<int:pk>', views.post_edit, name='post_edit'),
    path('account/register/', views.register, name='register'),
    path('accounts/login', views.Log, name='login'),
    path('accounts/logout', views.Log, name='logout'),
    path('upload/', views.image_upload_view, name='add_Image'),
    path('news/,', views.news, name='news'),
    path('about/', views.about_blog, name='about')
    
]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
