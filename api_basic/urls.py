from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from api_basic import views

from api_basic.views import CourseViewSet, UserViewSet, api_root
from rest_framework import renderers

router = DefaultRouter()
router.register(r'courses', views.CourseViewSet)
# router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.homePage, name='homepage'),
    path('course', views.coursePage, name='coursePage'),
    path('break', views.breakPage, name='breakPage'),
    path('list', views.display, name='courseDetail'),
    path('cart', views.cartPage, name='shoppingCart'),
    path('schedule', views.schedulePage, name='schedulePage'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
