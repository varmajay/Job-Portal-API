from dataclasses import field
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from .models import * 
from django.contrib.auth.hashers import make_password

class LoginSerializer(serializers.ModelSerializer):
    email =serializers.EmailField(max_length = 225)
    class Meta:
        model = User
        fields = ['email','password']
    

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','phone','password']

    def create(self, validated_data):
            validated_data['password'] = make_password(validated_data['password'])
            return super(UserCreateSerializer, self).create(validated_data)



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','phone','gender','address','profile']



class UserViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','phone','gender','address','profile']

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs 
        fields = ['id','hr','categories','type','position','salary','job_description','experience','vacancy']


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application 
        fields = ['job','name','email','phone','dob','gender','address','resume']