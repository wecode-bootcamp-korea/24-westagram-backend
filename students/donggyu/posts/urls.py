from django.urls import path

from .views      import PostCreateView, PostListView, UserPostListView, CommentCreateView, CommentListView

urlpatterns = [
    path('/1', PostCreateView.as_view()),
    path('/list', PostListView.as_view()),
    path('/userlist', UserPostListView.as_view()),
    path('/comment/1/<int:post_id>', CommentCreateView.as_view()),
    path('/commentlist/<int:post_id>', CommentListView.as_view())
]
