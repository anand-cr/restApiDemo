from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from profiles_api.models import ApiView
# Create your views here.


class HelloApiView(APIView):
    """Test API view"""
    serializer_class = serializers.HelloSerializer

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

# [ ]PUT AND DELETE ERROR
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
        api_function = ApiView.objects.get(pk=id)
        serializer = self.serializer_class(api_function, data=request.data)
        api_function.delete()

        return Response(serializer.data)
