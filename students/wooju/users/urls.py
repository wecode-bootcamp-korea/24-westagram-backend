from django.urls import path
from users.views import UsersView

urlpatterns = [
    path('', UsersView.as_view()),
]