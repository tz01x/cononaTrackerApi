from bangla.models import Division,City
from bangla.serializers import CitySerilizer,DivisionSerializer

from rest_framework import status
from rest_framework.response import Response
import  json
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
import datetime

from rest_framework import generics

class BangladeshDivisions(generics.ListCreateAPIView):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    permission_classes = []
    authentication_classes=[]


    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        # .filter(user=request.user)
        serializer = DivisionSerializer(queryset,many=True)
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CrateOrUpdate(request):
    try:
        division=request.POST.get('division',None)
        city=request.POST.get('city',None)
        namberofCases=request.POST.get('namberofCases',None)
        date=request.POST.get('date',None)
        # 'April 14, 2020'
        if date:
            date=datetime.datetime.strptime(date,'%B %d, %Y')
        # print(division)
        # print(city)
        # print(namberofCases)
        if division and city and namberofCases and date:
            division_obj,c=Division.objects.get_or_create(
            division=division,
            )
            division_obj.date=date
            division_obj.save()

            cityobjs=City.objects.all().filter(divi=division_obj,city=city)

            if len(cityobjs)==1:
                # update
                cityobj=cityobjs[0]
                cityobj.namberofCases=namberofCases
                cityobj.save()
            elif len(cityobjs)==0:
                # crate
                _cityobj=City.objects.create(
                divi=division_obj,
                city=city,
                namberofCases=namberofCases,
                date=division_obj.date
                )
                _cityobj.save()
                print(_cityobj.id,_cityobj)

                division_obj.city.add(_cityobj)
                division_obj.save()
            return Response({'details':"created"},status=status.HTTP_200_OK)



    except Exception as e:
        pass
    return Response({'details':"error occor"},status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)
