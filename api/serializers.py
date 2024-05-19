from rest_framework import serializers
from .models import WaitlistContact

class WaitListContactSerializer(serializers.ModelSerializer): 
    class Meta:
        model = WaitlistContact
        fields = '__all__'