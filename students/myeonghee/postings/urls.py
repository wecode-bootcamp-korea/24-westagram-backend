from postings.views import EnrollmentView

from django.urls import path

urlpatterns = [
    path("/enrollment",EnrollmentView.as_view())
]