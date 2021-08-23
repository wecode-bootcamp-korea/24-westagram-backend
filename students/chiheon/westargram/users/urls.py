from django.urls import path
from users.views import UserView

urlpatterns = [
        path('/signin', UserView.as_view()),
]
