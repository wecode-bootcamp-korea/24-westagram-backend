from django.urls import path
from users.views import SigninView, UsersView

urlpatterns = [
    path('/signup', UsersView.as_view()), 
    path('/signin', SigninView.as_view()),
]