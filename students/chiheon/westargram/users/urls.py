from django.urls import path
from users.views import UserView, Login

urlpatterns = [
        path('/signup', UserView.as_view()),
        path('/signin', Login.as_view()),
]
