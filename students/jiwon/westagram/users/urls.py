from django.urls import path
from users.views import UserView
# 최상위 url은 앱으로 연결 / 앱안의 url은 view로 연결

urlpatterns = [
    path('', UserView.as_view())
]
