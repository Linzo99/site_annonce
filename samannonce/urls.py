from django.contrib import admin
from django.urls import path, include
from post.views import PostListView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('annonces/', include('post.urls', namespace='post')),
    path('account/', include('account.urls', namespace='account')),
    path('', PostListView.as_view(), name='index')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)