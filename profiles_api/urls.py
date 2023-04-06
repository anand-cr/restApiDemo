# AttributeError: module 'django.views' has no attribute 'HeroViewSet' if we import from 'django' instead of '.'
from . import views
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename="hello-viewset")

urlpatterns = [
    # urls for APIView
    # path('', views.HelloApiView.as_view()),
    # path('update/<int:id>/', views.HelloApiView.as_view()),
    # path('delete/<int:id>/', views.HelloApiView.as_view()),

    # viewset
    path('', include(router.urls))

]

# urlpatterns = format_suffix_patterns(urlpatterns)
