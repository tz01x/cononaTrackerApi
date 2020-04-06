from django.http import JsonResponse,HttpResponse,HttpResponseBadRequest
from rest_framework import status
from rest_framework.response import Response
import  json
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from user.api.utils import  decode_uid
from main.serializers import  NewcasesSerialize,CountrySerializerDetails,CountrySerilis
from main.models import  Country,NewCases
from django.db.models import Q
from rest_framework import generics


class MyMessagesView2(generics.ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerilis
    permission_classes = []
    authentication_classes=[]


    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        # .filter(user=request.user)
        serializer = CountrySerilis(queryset,many=True)
        return Response(serializer.data)
import json
@api_view(['GET'])
@permission_classes([])
def CountryDetails(request,name):
    qs=Country.objects.filter(Q(country_name__icontains=name))


    if qs:
        newcases=qs[0].new_cases.all()
        labels=[]
        cases_nam=[]
        death_nam=[]
        for case in newcases:
            labels.append(case.date.strftime("%d %b"))
            cases_nam.append(case.new_cases)
            death_nam.append(case.new_death)
        s=CountrySerializerDetails(qs[0])
        # return Response(json.dumps(s.data))

        return Response({"data":s.data,
        "labels":labels,
        "new_cases":cases_nam,
        "new_death":death_nam})
    else:
        return Response({'detail':'no data found'},status=status.HTTP_404_NOT_FOUND)





import json,io,datetime
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createMessage(request):
    data=request.POST
    print(data)
    try:

        obj,isCreated=Country.objects.get_or_create(country_name=data.get('country_name'))

        if obj:
            obj.total_cases=data.get('total_cases')
            obj.total_death=data.get('total_death')
            obj.total_recover=data.get('total_recover')
            obj.active_cases=data.get('active_cases')
            obj.total_case_per_minion_pop=data.get('total_case_per_minion_pop')
            obj.total_death_per_minion_pop=data.get('total_death_per_minion_pop')
            obj.new_case=data.get('new_cases')
            obj.new_death=data.get('new_death')
            obj.save()
            if obj.new_cases.all().last().date==datetime.datetime.now().date():
                # update today cases
                last_new_case=obj.new_cases.all().last()
                last_new_case.new_cases=obj.new_case
                last_new_case.new_death=obj.new_death
                last_new_case.save()
            else:
                #create new one
                newcases=NewCases.objects.create(
                country=obj,
                new_cases=data.get('new_cases'),
                new_death=data.get('new_death')
                )
                obj.new_cases.add(newcases)


    except:
        return Response({'details':'error'},status=status.HTTP_200_OK)
    return Response({'details':'created'},status=status.HTTP_200_OK)
#     uid=None
#     text=None
#     try:
#         data=request.data
#         print(data)
#         # jdata=json.loads(data)
#         # print(jdata)
#         uid=data['uid']
#         text=data['text']
#         print(uid)
#     except Exception as e:
#         print(e)
#         print('data was send as a from-data')
#         uid=request.POST.get('uid',None)
#         text=request.POST.get('text',None)
#     finally:
#
#         if uid is None:
#             return Response({'detail':'Opps!, this link is invalid. Try a valid link '.title()},status=status.HTTP_403_FORBIDDEN)
#         user=decode_uid(uid)
#         if user is None:
#             return Response({'detail':'this link is invalid. Try a valid link '.title()},status=status.HTTP_403_FORBIDDEN)
#
#         msg=Message.objects.create(text=text)
#         myMessages,c=MyMessages.objects.get_or_create(user=user)
#         myMessages.messages.add(msg)
#         return Response({'detail':'message send'},status=status.HTTP_201_CREATED)
