from django.urls import path
from postings.views import PostingView, PostingGet

urlpatterns = [
        path('/addpost', PostingView.as_view()),
        path('/showpost', PostingGet.as_view()),
]
