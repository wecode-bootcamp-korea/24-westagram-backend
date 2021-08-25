from django.urls import path
from users.views import SignUpView

urlpatterns = [
    path('/sign-up', SignUpView.as_view()),
    path('/sign-in', SignUpView.as_view()),
]
