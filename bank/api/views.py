from rest_framework.views  import APIView
from rest_framework import generics
#from rest_framework.generics import ListAPIView
from rest_framework.response import Response 
from bank.models import bank_info
from .serializers import BankSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters  import SearchFilter , OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated



class BankAPIViewPagination(LimitOffsetPagination):    #to add pagination creating the pagination class
	default_limit = 50
	max_limit = 100



class  BankAPIView(generics.ListAPIView):
	permission_classes 		= [IsAuthenticated]
	authentication_classes 	= [SessionAuthentication]
	queryset                = bank_info.objects.all()
	serializer_class        = BankSerializer
	pagination_class 		= BankAPIViewPagination
	filter_backends 		= [SearchFilter,OrderingFilter,DjangoFilterBackend]
	search_fields			= ['ifsc']
	filterset_fields  		= ['bank_name','city']
	




class  BankCreateAPIView(generics.CreateAPIView):
	permission_classes 		= [IsAuthenticated]
	authentication_classes 	= [SessionAuthentication]
	queryset                = bank_info.objects.all()
	serializer_class        = BankSerializer



class  BankDetailAPIView(generics.RetrieveAPIView):
	permission_classes 		= [IsAuthenticated]
	authentication_classes 	= [SessionAuthentication]
	queryset                = bank_info.objects.all()
	serializer_class        = BankSerializer
	#lookup_field			= 'ifsc'



class  BankUpdateAPIView(generics.UpdateAPIView):
	permission_classes 		= [IsAuthenticated]
	authentication_classes 	=[SessionAuthentication]
	queryset                = bank_info.objects.all()
	serializer_class        = BankSerializer
	#lookup_field 			= 'ifsc'


class  BankDeleteAPIView(generics.DestroyAPIView):
	permission_classes 		= [IsAuthenticated]
	authentication_classes 	= [SessionAuthentication]
	queryset                = bank_info.objects.all()
	serializer_class        = BankSerializer
	#lookup_field 			= 'ifsc'





