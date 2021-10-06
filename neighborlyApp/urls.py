"""neighborlyApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from neighborlyUsers import views
from posts.views import add_post_view as add_post

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='index'),
    path('register/', views.register, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_action, name='logout'),
    path('addpost/', add_post, name="addpost"),
]
