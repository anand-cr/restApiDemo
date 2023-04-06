from rest_framework import serializers

from profiles_api.models import ApiView


class HelloSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes a name field for testing our APIView"""
    # name = serializers.CharField(max_length=10)
    # id = serializers.IntegerField()
    function = serializers.CharField(max_length=50)
    details = serializers.CharField(max_length=100)

    class Meta:
        model = ApiView
        fields = ('id', 'function', 'details')
