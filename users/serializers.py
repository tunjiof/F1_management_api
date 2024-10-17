from rest_framework import serializers
from .models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'password2','role')

    def validate(self, data):
        print("from validation: ", data)
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "password must match"})
        
        #validate password strength
        validate_password(data['password'])
        return data

    def create(self, validated_data):
        print("from create method: ", validated_data)
        user = User(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            role=validated_data['role']
        )

        user.set_password(validated_data['password'])
        user.save()
        return user