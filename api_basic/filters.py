import django_filters

from .models import Course


class CourseFilter(django_filters.FilterSet):

    class Meta:
        model = Course

        # fields = ['subject']
        fields = ['subject', 'catalog_number',
                  'instructor', 'credit', 'meeting_time']
        # fields = '__all__'
