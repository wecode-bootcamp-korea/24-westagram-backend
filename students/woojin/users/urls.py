from django.urls import path
from users.views import UsersView

urlpatterns = [
    path('/signup', UsersView.as_view()),
]