from.models import ProductModel
from rest_framework import serializers

class Productser(serializers.ModelSerializer):
    class Meta:
        model=ProductModel
        fields='__all__'