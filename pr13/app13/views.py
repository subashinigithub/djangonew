from django.shortcuts import render
from rest_framework import serializers
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import *


@api_view(['GET'])
def apioverview(r):
    api_urls={
        'all_items':'/all/',
        'search by name':'/?name=name_name',
        'search by designation':'/?designation_name',
        'Add':'/create',
        'Update':'/update/pk',
        'Delete':'/employee/pk/delete'
    }
    return Response(api_urls)


@api_view(['POST'])
def add_items(r):
    emp=empserializer(data=r.data)
    if employee.objects.filter(**r.data).exists():
        raise serializers.ValidationError('This data already exists')
    if emp.is_valid():
        emp.save()
        return Response(emp.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])
def view_items(r):
    if r.query_params:
        emp=employee.objects.filter(**r.query_params.dict())
    else:
        emp=employee.objects.all()
    if emp:
        serializer=empserializer(emp,many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def update_items(r,pk):
    emp=employee.objects.get(pk=pk)
    data=empserializer(instance=emp,data=r.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['GET'])   
def delete(r,pk):
        emp = employee.objects.get(pk=pk)
        
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



