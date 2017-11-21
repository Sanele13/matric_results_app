from rest_framework import serializers
from .models import matric_app_model

class matric2016_serializer(serializers.ModelSerializer):
    class Meta:
        model = matric_app_model
        fields = ('id', 'emis', 'centre_no', 'name','wrote_2014','passed_2014','wrote_2015','passed_2015','wrote_2016','passed_2016')