from django.urls import path

from .views import PostsDetail, PostsList

urlpatterns = [
    path("", PostsList.as_view(), name="posts_list"),
    path("blog/<int:pk>/", PostsDetail.as_view(), name="posts_detail"),
]
