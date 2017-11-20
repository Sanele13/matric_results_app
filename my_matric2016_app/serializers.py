from rest_framework import serializers
from .models import matric_app_model

class matric2016_serialiser(serializers.ModelSerializers):
    class Meta:
        model = matric_app_model
        fields = ('id', 'emis', 'centre_no', 'name','wrote2014','wrote2014','wrote2015','wrote2015','wrote2016','wrote2016')