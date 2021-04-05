from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from api_basic import views

from api_basic.views import CourseViewSet, UserViewSet, api_root
from rest_framework import renderers

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    #path('', include(router.urls)),
    path('', views.homePage, name='homepage'),
    path('homepage/course', views.coursePage, name='coursePage'),
    path('homepage/break', views.breakPage, name='breakPage'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
