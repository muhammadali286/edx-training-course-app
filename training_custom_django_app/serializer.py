from rest_framework import serializers 

from openedx.core.djangoapps.content.course_overviews.models import CourseOverview


class CourseCustomSerializer(serializers.ModelSerializer):

    class Meta:
        model = CourseOverview
        fields = ('id', 'org', 'display_name', '_location', 'language')