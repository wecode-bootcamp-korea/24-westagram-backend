from django.urls import path
from users.views import LoginsView, UsersView

urlpatterns = [
    path('/sign-up', UsersView.as_view()),
    path('/login', LoginsView.as_view()),
]  