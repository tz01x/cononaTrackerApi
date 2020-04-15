from rest_framework import serializers
from .models import Division,City

class CitySerilizer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=['city','namberofCases']

class DivisionSerializer(serializers.ModelSerializer):
    city=CitySerilizer(many=True)
    date= serializers.DateTimeField(format="%B %d, %Y", required=False, read_only=True)

    class Meta:
        model=Division
        fields=[
        'division',
        'city',
        'date'
        ]
