from rest_framework import serializers
from django.shortcuts import render
from .models import Pos
from rest_framework import viewsets
from snipapp.serializers import PosSerializer
from rest_framework import generics


# Create your views here.
def import_db(request):
    
    f = open('/home/sandeep/Desktop/new/snip/snipapp/csv/all_india_pin_code.csv', 'r')  
    for line in f:
        line =  line.split(',')
        tmp = Pos.objects.create()
        tmp.officename = line[0]
        tmp.pincode= line[1]
        tmp.officeType = line[2]
        tmp.Deliverystatus = line[3]
        tmp.divisionname = line[4]
        tmp.regionname = line[5]
        tmp.circlename = line[6]
        tmp.taluk = line[7]
        tmp.Districtname = line[8]
        tmp.statename = line[9]
    	tmp.save()

    f.close()



class PosViewSet(generics.ListCreateAPIView):
    queryset = Pos.objects.all()
    serializer_class = PosSerializer


class PosList(generics.ListCreateAPIView):
    serializer_class=PosSerializer 
    def get_queryset(self):
        PINCODE=self.kwargs['PINCODE']
        return Pos.objects.filter(pincode=PINCODE)
        '''PINCODE = self.request.query_params.get('PINCODE', None)
        if PINCODE is not None:
            queryset = queryset.filter(pincode=PINCODE)
        return queryset'''


         
