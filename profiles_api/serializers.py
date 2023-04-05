from rest_framework import serializers

from profiles_api.models import ApiView


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

    # class Meta:
    #     model = ApiView
    #     fields = ('id', 'function', 'details')
