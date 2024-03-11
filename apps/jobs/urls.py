from django.urls import path
from .views import JobsView , JobsDetail



urlpatterns = [
    path(
        "jobs/",
        JobsView.as_view(template_name="jobs.html"),
        name="jobs",
    ),
    path(
        "jobs/job_detail",
        JobsDetail.as_view(template_name="job_detail.html"),
        name="jobs/job_detail",
    )
]
