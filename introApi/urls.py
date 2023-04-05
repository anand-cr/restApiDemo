# AttributeError: module 'django.views' has no attribute 'HeroViewSet' if we import from 'django' instead of '.'
from . import views
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
# router = routers.DefaultRouter()

# router.register(r'heroes', views.HeroViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('heroes/', views.Hero_list),
    path('heroes/<int:id>', views.Hero_details)
]

urlpatterns = format_suffix_patterns(urlpatterns)
