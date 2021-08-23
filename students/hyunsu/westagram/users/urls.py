from django.urls import path

from users.views import UserSign, UserView

urlpatterns = [
    path('/signup', UserView.as_view()),
    path('/signin', UserSign.as_view())
]
