from django.urls import path 
from users.views import Signup

urlpatterns = [
    path('',Signup.as_view()),
]
