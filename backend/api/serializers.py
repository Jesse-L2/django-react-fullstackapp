from django.contrib.auth.models import User
from rest_framework import serializers

# Django uses an ORM (object relational mapping), serializer converts the python object to json data and vice versa

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password' ]
        extra_kwargs = {'password': {'write_only': True}} # no one can read the password

    def create(self, validated_data):
        # validated data has been validated by serializer
        user = User.objects.create_user(**validated_data)
        return user
