from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework.reverse import reverse
from rest_framework import viewsets

from rest_framework.decorators import action

from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User

from api_basic.models import Course
from api_basic.serializers import CourseSerializer, UserSerializer
from api_basic.permissions import IsOwnerOrReadOnly

from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.list import ListView

from .filters import CourseFilter

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'courses': reverse('course-list', request=request, format=format)
    })


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


def display(request):
    context = {}
    filtered_course = CourseFilter(
        request.GET,
        queryset=Course.objects.all()
    )

    context['filtered_courses'] = filtered_course

    # try:
    #     context = paginator.page(page)

    # except PageNotAnInteger:
    #     context = paginator.page(1)

    # except EmptyPage:
    #     context = paginator.page(paginator.num_pages)

    context['filtered_courses'] = filtered_course

    # course_list = Course.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(filtered_course.qs, 25)
    course_page_obj = paginator.get_page(page)

    context['course_page_obj'] = course_page_obj

    return render(request, 'courseDetail.html', context=context)
    # return render(request, 'courseDetail.html', {'courses': courses})
# view function for home page of site.


def homePage(request):
    return render(request, 'homepage.html')

# view function for add a course page


def coursePage(request):
    return render(request, 'coursePage.html')


def breakPage(request):
    return render(request, 'breakPage.html')
