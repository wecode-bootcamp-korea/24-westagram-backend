from django.urls import path
from .views import AddPostingView, UserPostingView, AddCommentView, PostcommentingView, ToggleLikeView, ToggleFollowView, PostingView, CommentView

urlpatterns = [
    path("/posting", AddPostingView.as_view()),
    path("/posting/user/<int:user_id>", UserPostingView.as_view()),
    path("/posting/<int:post_id>", PostingView.as_view()),
    path("/posting/<int:post_id>/comment", PostcommentingView.as_view()),
    path("/comment", AddCommentView.as_view()),
    path("/comment/<int:comment_id>", CommentView.as_view()),
    path("/liking", ToggleLikeView.as_view()),
    path("/following", ToggleFollowView.as_view()),
]