from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from notifications import views

urlpatterns = [
    path('notifications/<int:id>/', views.notification_view, name="notifications"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)