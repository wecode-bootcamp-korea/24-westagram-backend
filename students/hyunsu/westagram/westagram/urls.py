from django.urls import path, include

urlpatterns = [
    path('user', include('users.urls')),
]
