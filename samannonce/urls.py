from django.contrib import admin
from django.urls import path, include
from post.views import PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('annonces/', include('post.urls', namespace='post')),
    path('account/', include('account.urls', namespace='account')),
    path('', PostListView.as_view(), name='index')
]
