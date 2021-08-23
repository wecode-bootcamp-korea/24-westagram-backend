from django.urls import path
from users.views import SignUpView

urlpatterns = [
    path('/sign_up', SignUpView.as_view()),
]
