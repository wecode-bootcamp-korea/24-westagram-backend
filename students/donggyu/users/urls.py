from django.urls import path

from .views      import SinupView
urlpatterns = [
    path('/signup', SinupView.as_view()),
]
