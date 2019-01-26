from rest_framework import serializers
from courses.models import Course


class CourseSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Course
        fields = ('title','id')
