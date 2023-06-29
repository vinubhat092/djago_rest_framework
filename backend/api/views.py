from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
from django.forms.models import model_to_dict
# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request,*args,**kwargs):
    
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # data = request.data
    # return Response(data)

    