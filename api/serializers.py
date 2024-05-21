from rest_framework import serializers
from .models import WaitlistContact

class WaitListContactSerializer(serializers.ModelSerializer): 

    read_only_fields = ['subscription_status']
    class Meta:
        model = WaitlistContact
        fields = '__all__'