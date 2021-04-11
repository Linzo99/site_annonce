from django.urls import path
from . import views

app_name="post"

urlpatterns = [
    path('d/<slug:slug>', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>', views.PostListView.as_view(), name='post_list_by_slug'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('', views.PostListView.as_view(), name='post_list')
]