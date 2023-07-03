from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields=['id','name','price']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rating
        fields="_all_"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields="_all_"