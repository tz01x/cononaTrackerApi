from rest_framework import serializers
from .models import  Country,NewCases
from django.contrib.auth.models import User

class NewcasesSerialize(serializers.ModelSerializer):
    date= serializers.DateField(format="%d-%m-%Y", required=False, read_only=True)
    class Meta:
        model=NewCases
        fields=['new_cases','new_death','date']
        read_only_fields = ['id']

class CountrySerializerDetails(serializers.ModelSerializer):
    new_cases=NewcasesSerialize(many=True)
    class Meta:
        model=Country
        fields=['new_cases','country_name',
                'new_case',
                'new_death',
                'total_cases',
                'total_death',
                'total_recover',
                'active_cases',
                'total_case_per_minion_pop',
                'total_death_per_minion_pop'
    ]

class CountrySerilis(serializers.ModelSerializer):
    class Meta:
        model=Country

        exclude=['new_cases','id']


# class UserS(serializers.ModelSerializer):
#     class Meta:
#         model=User
#         fields=['username']
#
# class StringSerializer(serializers.StringRelatedField):
#
#     def to_internal_value(self,value):
#         return value
#
#
# class MyMessagesSerializer(serializers.ModelSerializer):
#     messages=messageSerializer(many=True)
#     user=StringSerializer()
#     # messages = StringSerializer(many=True)
#     class Meta:
#         model = MyMessages
#         fields=('id','user','messages')
        # read_only_fields = ['user',]?
# from main.models import MyMessages
# from main.serializers import MyMessagesSerializer
# qs=MyMessages.objects.all()
