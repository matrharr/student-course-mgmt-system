from rest_framework import serializers
from students.models import Student
from courses.serializers import CourseSerializer

class StudentSerializer(serializers.Serializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student
        fields = ('name')
