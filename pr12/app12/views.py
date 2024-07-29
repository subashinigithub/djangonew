from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializer import ItemSerializer


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_items': '/all/',
        'Search by Category': '/?category=category_name',
        'Search by Subcategory': '/?subcategory=category_name',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/item/pk/delete'
    }

    return Response(api_urls)
from rest_framework import serializers
from rest_framework import status

@api_view(['POST'])
def add_items(request):
    item = ItemSerializer(data=request.data)

    if Item.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



