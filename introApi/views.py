from django.http import JsonResponse
from django.shortcuts import render
from .serializers import HeroSerializer
from .models import Hero
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.


# TypeError: api_view() takes from 0 to 1 positional arguments but 2 were given
@api_view(['GET', 'POST'])
def Hero_list(request, format=None):

    if request.method == 'GET':
        """Get the data -> serialise it -> output json  """
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        # return JsonResponse({'heroes': serializer.data})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'POST':
        """Take json data -> deserialise -> """
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# class HeroViewSet(viewsets.ModelViewSet):
#     """get request"""
#     queryset = Hero.objects.all().order_by('name')
#     serializer_class = HeroSerializer


@api_view(['GET', 'PUT', 'DELETE'])
def Hero_details(request, id, format=None):

    try:
        hero = Hero.objects.get(pk=id)
    except Hero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HeroSerializer(hero)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HeroSerializer(hero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        hero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIview features"""
        an_apiview = [

        ]
