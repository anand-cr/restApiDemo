from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated

from profiles_api import serializers, models
from profiles_api.models import ApiView, UserProfile
from profiles_api import permissions

# Create your views here.

# For the profile view


class UserProfileViewSet(viewsets.ModelViewSet):
    """handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # authentication class - mechanism of authentication
    # permission classes - what permissions given to users
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')  # DRF will allow us to search by these

    # def list(self, request):
    #     profiles = self.queryset
    #     serializer = self.serializer_class(profiles, many=True)
    #     return Response({"test"})


class UserLoginApiView(ObtainAuthToken):
    """handle creating user authentication tokens"""
    # This provides the ability to modify the data after we get the authentication
    # section 11: Craete login API
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedItemView(viewsets.ModelViewSet):
    """handles creating, reading and updating profile feed item"""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()

    # Thsi will add
    # https://detecttechnologies.udemy.com/course/django-python/learn/lecture/6955156#questions/13213586
    permission_classes = (
        permissions.UpdateOwnStatus,
        IsAuthenticated  # unlike the readonly this will completely restrict if not authenticated
        # if not authenticated -> readonly #? is any authentication enough, why use this
        # IsAuthenticatedOrReadOnly,

    )

    # default behavour -> when a request is made to viewset, it is passed into the serializer , validated and serialser.save() is called by default
    # called for every HTTP post
    # lecture 63: https://detecttechnologies.udemy.com/course/django-python/learn/lecture/6955146#questions/11360600
    # https://detecttechnologies.udemy.com/course/django-python/learn/lecture/6955146#questions/4392484
    # https://detecttechnologies.udemy.com/course/django-python/learn/lecture/6955146#questions/6199996
    def perform_create(self, serializer):
        """sets the user profile to be logged in user"""
        # user_profile is passed in in addition to all the items in serializer
        # if user has been authenticated, then user field will be there else an anon user
        # NOTE: doubt
        serializer.save(user_profile=self.request.user)

  # -------------------------------------------------------------------


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer
    # [ ]put all the requests in try except block

    def get(self, request):
        """returns a list of APIView features"""
        api_functions = ApiView.objects.all()  # NOTE: ApiView here is the model name
        serializer = self.serializer_class(api_functions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        # an_apiview = {
        #     'Uses HTTP methods as function (get, post, patch, put, delete)',
        #     'Is similar to a traditional Django View',
        #     'Gives you the most control over you application logic',
        #     'Is mapped manually to URLs',
        # }
        # return Response({'message': 'functionality of APIview', 'functionality': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # name = serializer.validated_data.get('name')
            # message = f'Hello {name}'
            # return Response({'message': message})
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        """handle updating an object"""
        api_function = ApiView.objects.get(pk=id)
        serializer = self.serializer_class(api_function, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # return Response({'method': 'PUT'})

    def delete(self, request, id):
        api_function = ApiView.objects.get(id=id)  # ApiView is the modal name
        api_function.delete()
        return Response({'message': 'ApiView feature deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class HelloViewSet(viewsets.ViewSet):
    """Test API viewset"""
    serializer_class = serializers.HelloSerializer
    # query_list = ApiView.objects.all()

    def list(self, request):
        """returns the list of functions"""
        feature_list = ApiView.objects.all()
        serializer = self.serializer_class(feature_list, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        feature = ApiView.objects.get(pk=pk)
        serializers = self.serializer_class(feature)
        return Response(serializers.data)

    def create(self, request):

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
