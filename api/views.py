from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from .models import WaitlistContact
from .serializers import WaitListContactSerializer

@api_view(['POST'])
def add_to_waitlist(request):
    try:
        data = JSONParser().parse(request)
        serializer = WaitListContactSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()

            # Initialize Mailchimp client
            mailchimp = Client()
            mailchimp.setConfig({
                "api_key": "e01ade4d0e977bb47335bca8f4f0c065-us21",
                "server": "us21"
            })
            
            # Retrieve list ID and prepare member info
            list_id = "AFROVIVO_WAITLIST_ID"
            member_info = {
                "email_address": serializer.validated_data['email'],
                "status": serializer.validated_data['subscription_status'],
            }

            # Add member to Mailchimp list
            res = mailchimp.lists.add_list_member(list_id, member_info)
            print("res: {}".format(res))
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except ApiClientError as error:
        print("An exception occurred: {}".format(error.text))
        return Response({"error": "An error occurred while connecting to Mailchimp."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
