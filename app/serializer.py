from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):
    # date_uploaded = serializers.DateField(format="%Y-%m-%d")
    # time_uploaded = serializers.TimeField(format="%H:%M")

    class Meta:
        model = Products
        fields = ['id', 'title', 'description']


