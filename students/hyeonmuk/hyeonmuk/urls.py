from django.urls import path
from django.urls.resolvers import URLPattern
from hyeonmuk.views import UsersView

urlpatterns = [
    path('/users', UsersView.as_view()), 
]