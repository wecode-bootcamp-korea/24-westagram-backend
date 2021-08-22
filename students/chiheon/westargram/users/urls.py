from django.urls import path
from users.views import *

urlpatterns = [
        path('signin', UserView.as_view()),
        ]
