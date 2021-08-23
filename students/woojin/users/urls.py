from django.urls import path
from users.views import UsersView, LoginsView

urlpatterns = [
    path('/signup', UsersView.as_view()),
    path('/login', LoginsView.as_view()),
]