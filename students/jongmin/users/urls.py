from django.urls import path 

from users.views import Signup, Login

urlpatterns = [
    path('/signup',Signup.as_view()),
    path('/login',Login.as_view()),
]
