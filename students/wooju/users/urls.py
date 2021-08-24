from django.urls import path
from users.views import UsersView

urlpatterns = [
    path('/sign-up', UsersView.as_view()),
]  