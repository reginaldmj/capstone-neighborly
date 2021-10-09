from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from posts import views

urlpatterns = [
    path('addpost/', views.add_post_view, name="addpost"),
    path('post/<int:id>/', views.Post_View, name="post"),
    path('like/<int:post_id>/', views.like, name='like'),
    path('dislike/<int:post_id>/', views.dislike, name='dislike')

]

