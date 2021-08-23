from django.urls import path
from .views import SignUp, Login

app_name = "users"

urlpatterns = [
    path("/signup", SignUp.as_view()),
    path("/login", Login.as_view()),
]
