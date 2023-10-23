from rest_framework import filters
from rest_framework.generics import ListAPIView

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview
from .serializer import CourseCustomSerializer


class CustomCourseListView(ListAPIView):
    queryset = CourseOverview.objects.all()

    filter_backends = [filters.SearchFilter]
    search_fields = ['language', 'display_name']

    serializer_class = CourseCustomSerializer