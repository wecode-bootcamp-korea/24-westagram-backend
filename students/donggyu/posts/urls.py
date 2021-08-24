from django.urls import path

from .views      import PostCreateView, PostListView, UserPostListView

urlpatterns = [
    path('/1', PostCreateView.as_view()),
    path('/list', PostListView.as_view()),
    path('/userlist', UserPostListView.as_view())
]
