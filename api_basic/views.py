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
from cart.models import *
import re
import datetime
import time


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

    # add to shopping cart

    if request.method == 'POST':
        print(request.POST.getlist('checked_selection'))
        course_ids = request.POST.getlist('checked_selection')
        user = request.user
        print(user)
        if user.is_authenticated:
            print(Cart.objects.filter(user=user))
            curr_cart = Cart.objects.filter(user=user)[0]
            curr_cart_items = CartItem.objects.filter(cart=curr_cart)
            for item in curr_cart_items:
                print(item.product.course_id)

            for course_id in course_ids:
                course = Course.objects.get(pk=course_id)
                cart_item = CartItem(user=user, cart=curr_cart, product=course)
                cart_item.save()

        return render(request, 'homepage.html')
        # for id in course_ids:

    context = {}
    print(request.GET)
    filtered_course = CourseFilter(
        request.GET,
        queryset=Course.objects.all()
    )
    context['filtered_courses'] = filtered_course

    # course_list = Course.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(filtered_course.qs, 25)
    course_page_obj = paginator.get_page(page)

    context['course_page_obj'] = course_page_obj

    return render(request, 'courseDetail.html', context=context)

# view function for home page of site.


def homePage(request):
    return render(request, 'homepage.html')

# view function for add a course page


def coursePage(request):
    return render(request, 'coursePage.html')


def breakPage(request):
    return render(request, 'breakPage.html')


def schedulePage(request):
    return render(request, 'schedulepage.html')


def cartPage(request):
    context = {}
    cart_course = []
    user = request.user
    if user.is_authenticated:
        curr_cart = Cart.objects.filter(user=user)[0]
        curr_cart_items = CartItem.objects.filter(cart=curr_cart)
        print(curr_cart_items)
        for item in curr_cart_items:
            print(Course.objects.get(pk=item.product.course_id))
            cart_course.append(Course.objects.get(pk=item.product.course_id))

        context['cart_courses'] = cart_course

    if request.method == 'POST':
        # DELETE FEATURE
        if 'delete_course' in request.POST:
            print(request.POST.getlist('checked_selection'))
            course_ids = request.POST.getlist('checked_selection')
            user = request.user
            print(user)
            if user.is_authenticated:
                print(Cart.objects.filter(user=user))
                curr_cart = Cart.objects.filter(user=user)[0]
                curr_cart_items = CartItem.objects.filter(cart=curr_cart)

                for course_id in course_ids:
                    instance = CartItem.objects.filter(
                        user=user).filter(product=int(course_id))
                    instance.delete()
            return render(request, 'homepage.html')

        # SCHEDULE GENERATE FEATURE -- TODO
        elif 'create_schedule' in request.POST:
            #     schedule_context = {}
            #     course_ids = request.POST.getlist('checked_selection')
            #     user = request.user
            #     print(user)
            #     if user.is_authenticated:
            #         for course_id in course_ids:
            #             course = Course.objects.get(pk=course_id)
            #             time = course.meeting_time
            #             tmp = time.split(" ", 1)
            #             days = re.findall('[A-Z][^A-Z]*', tmp[0])
            #             schedule = tmp[1]

            #             for day in days:
            #                 if day not in schedule_context:
            #                     schedule_context[day] = []
            #                 schedule_context[day].append(schedule)

            #         for key in schedule_context:
            #             q = []
            #             for s in schedule_context[key]:
            #                 q.append(s.split(' - '))
            #             tformat = '%I:%M %p'
            #             time_hours = [time.strptime(t[0], tformat) for t in q]
            #             time_hours_end = [time.strptime(t[1], tformat) for t in q]
            #             result = [time.strftime(tformat, h)
            #                       for h in sorted(time_hours)]
            #             result_end = [time.strftime(tformat, h)
            #                           for h in sorted(time_hours_end)]

            #             res = []
            #             for i in range(len(result)):
            #                 res.append([f'{result[i]} - {result_end[i]}'])
            #             schedule_context[key] = res

            return render(request, 'schedulepage.html')

    return render(request, 'shoppingCart.html', context=context)
