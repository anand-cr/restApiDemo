# AttributeError: module 'django.views' has no attribute 'HeroViewSet' if we import from 'django' instead of '.'
from . import views
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.HelloApiView.as_view()),


]

urlpatterns = format_suffix_patterns(urlpatterns)
