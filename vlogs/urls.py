from django.urls import path

from .views import VPostsDetail, VPostsList

urlpatterns = [
    path("", VPostsList.as_view(), name="posts_list"),
    path("<int:pk>", VPostsDetail.as_view(), name="posts_detail"),
]
