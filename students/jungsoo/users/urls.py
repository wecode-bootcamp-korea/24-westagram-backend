from users.views import CreateView

from django.urls import path

urlpatterns = [
    path('create/', CreateView.as_view()),
]