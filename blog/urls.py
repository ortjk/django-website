from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_home),
    path('create/', views.create_post),
    path('view/<int:post_id>', views.view_blog_post, name="view_blog_post")
]
