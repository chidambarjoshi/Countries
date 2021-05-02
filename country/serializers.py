from django.db.models import fields
from rest_framework import serializers
from .models import City,Image

class CitySerializer(serializers.ModelSerializer):
     class Meta:
         model= City
         fields =('city','state','country')


class ImageSerializer(serializers.ModelSerializer):
    
    image=serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    class Meta:
        model = Image
        fields = (
            'image',
            'image_name',
            
        )

    