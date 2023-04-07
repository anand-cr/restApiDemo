# AttributeError: module 'django.views' has no attribute 'HeroViewSet' if we import from 'django' instead of '.'
from . import views
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename="hello-viewset")
# only need to write basename if queryset is not there
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.ProfileFeedItemView)

urlpatterns = [
    # urls for APIView
    # path('', views.HelloApiView.as_view()),
    # path('update/<int:id>/', views.HelloApiView.as_view()),
    # path('delete/<int:id>/', views.HelloApiView.as_view()),

    # viewset
    # The login endpoint doesn't really fit into the Create, Read, Update, Delete model that the viewsets are based on, so we create a separate endpoint for that.
    path('login/', views.UserLoginApiView.as_view()),

    # This includes all create read update delete
    path('', include(router.urls))

]

# urlpatterns = format_suffix_patterns(urlpatterns)
