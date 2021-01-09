from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import discounTypeSerializer
from .models import discounType
from rest_framework.response import Response
from rest_framework import status
from .passwordHandle import PasswordHandle
# Create your views here.

@api_view(['POST'])
def verify_discount(request):
    if request.method == 'POST':
        password = request.data['password']
        discoun_type = request.data['datatypes_id']
        try:
            discount_obj = discounType.objects.get(id=discoun_type)
        except:
            raise discounType.DoesNotExist('data does not match')
        my_pass_hndlr = PasswordHandle()
        valid = my_pass_hndlr.verify_password(discount_obj.password, password)
        print(valid)
        serializer = discounTypeSerializer(discount_obj, many=False)
        if valid: 
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'password is not matching'}, status=status.HTTP_400_BAD_REQUEST)
