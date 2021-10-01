from rest_framework import serializers
from execution.models import Guest, HouseNo

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = HouseNo
        fields = ['number']

class GuestSerializer(serializers.ModelSerializer):
    house_key = HouseSerializer()
    class Meta:
        model = Guest
        fields = ['guest_name','mobile_number','house_key']
