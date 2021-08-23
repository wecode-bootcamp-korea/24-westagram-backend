from . import views

from django.urls import path



app_name="users"
urlpatterns = [
    path("/signin",views.SignInView.as_view())
]
