from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from neighborlyUsers import views

urlpatterns = [
    path('', views.homepage_view, name='index'),
    path('register/', views.register, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_action, name='logout')

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)