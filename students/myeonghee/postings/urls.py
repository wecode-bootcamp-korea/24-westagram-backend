from django.urls import path

from postings.views import EnrollmentView, CommentView


urlpatterns = [
    path("/enrollment",EnrollmentView.as_view()),
    path("/comment",CommentView.as_view())
]
    # path("/<int:post_id>/comment",CommentView.as_view())