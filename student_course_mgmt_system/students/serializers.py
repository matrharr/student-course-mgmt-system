from rest_framework import serializers
from students.models import Student
from courses.serializers import CourseSerializer

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=50)
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = '__all__'
