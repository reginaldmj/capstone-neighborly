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
from location.views import location_search
from posts import views as post_views
from django.conf import settings
from django.conf.urls.static import static
from notifications import views as notif_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage_view, name='index'),
    path('register/', views.register, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_action, name='logout'),
    path("location/", location_search, name="location"),
    path('addpost/', post_views.add_post_view, name="addpost"),
    path("post/<int:id>/", post_views.Post_Detail_View.as_view(), name="post"),
    path('post/<int:id>/edit/', post_views.edit_post_view, name="editpost"),
    path('post/<int:id>/delete/',post_views.delete_post_view,name='delete'),
    path('notifications/<int:id>/',notif_views.notification_view, name="notifications"),
    path('profile/<int:id>/', views.profile, name="profile"),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
