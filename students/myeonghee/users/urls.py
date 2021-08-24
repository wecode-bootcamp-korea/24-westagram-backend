from users.views import SignUpView, SignInView

from django.urls import path

urlpatterns = [
    path("/signup",SignUpView.as_view()),
    path("/signin",SignInView.as_view())
]
