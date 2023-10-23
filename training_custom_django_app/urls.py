"""
URLs for training_custom_django_app.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import

from .views import CustomCourseListView

urlpatterns = [
    re_path(r'/courses/', CustomCourseListView.as_view(), name="course-list"),
]
