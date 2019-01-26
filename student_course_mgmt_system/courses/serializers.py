from rest_framework import serializers
from courses.models import Course
# from students.serializers import StudentSerializer

class CourseSerializer(serializers.ModelSerializer):

    # students = StudentSerializer(many=True)

    class Meta:
        model = Course
        fields = ('title',)
