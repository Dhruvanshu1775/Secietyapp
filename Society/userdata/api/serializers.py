from django.rest_framework import serializers
from userdata.models import package/module

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
