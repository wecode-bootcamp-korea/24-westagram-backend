from django.urls import path
from users.views import SigninView, UsersView

urlpatterns = [
    path('', UsersView.as_view()), 
    path('/signin', SigninView.as_view())
]