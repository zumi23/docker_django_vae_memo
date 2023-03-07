from django.contrib import admin
from django.urls import path, include

# アップロードした画像を表示するための設定
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('application.urls')),
    path('vaes/', include('vaes.urls')),
]

# アップロードした画像を表示するための設定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

