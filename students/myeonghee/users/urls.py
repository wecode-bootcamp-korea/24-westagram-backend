from . import views

from django.urls import path

urlpatterns = [
    path("/signup",views.SignUpView.as_view()),
    path("/signin",views.SignInView.as_view())
]
