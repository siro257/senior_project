from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course


class UserSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Course.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'courses']


class CourseSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Course
        # fields = ['owner', 'course_id', 'course_title',
        #           'instructor', 'credit', 'semester_offered']
        fields = '__all__'
