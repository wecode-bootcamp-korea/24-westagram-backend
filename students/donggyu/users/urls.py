from django.urls import path

from .views      import SinupView, LoginView

urlpatterns = [
    path('/signup', SinupView.as_view()),
    path('/login', LoginView.as_view()),
]
