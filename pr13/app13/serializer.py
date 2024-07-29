from django.db.models import fields
from rest_framework import serializers
from .models import *


class empserializer(serializers.ModelSerializer):
    class Meta:
        model=employee
        fields=['name','age','salary','designation','experience','gender']