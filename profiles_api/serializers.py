from rest_framework import serializers

from profiles_api.models import ApiView, UserProfile
from profiles_api import models


class HelloSerializer(serializers.HyperlinkedModelSerializer):
    """Serializes a name field for testing our APIView"""
    # name = serializers.CharField(max_length=10)
    # id = serializers.IntegerField()
    function = serializers.CharField(max_length=50)
    details = serializers.CharField(max_length=100)

    class Meta:
        model = ApiView
        fields = ('id', 'function', 'details')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,  # the password can only be used to update or create new instances, but not to retrieve existing instances
                'style': {'inout_type': 'password'}
            }
        }

    # NOTE: make sure it is not inside the meta class
    # Create is a inbuld function but we override it to make it call our custom create user instaed of the inbuilt one
    def create(self, validated_data):
        """create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    # NOTE: why?
    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
