from django.urls import path

from users.views import CreateView

urlpatterns = [
    path('/create', CreateView.as_view()),
]