from rest_framework.views  import APIView
from rest_framework import generics
#from rest_framework.generics import ListAPIView
from rest_framework.response import Response 
from bank.models import bank_info
from .serializers import BankSerializer
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters  import SearchFilter , OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



class BankAPIViewPagination(LimitOffsetPagination):    #to add pagination creating the pagination class
	default_limit = 50
	max_limit = 100



class  BankAPIView(generics.ListAPIView):
	permission_classes 		= []
	authentication_classes 	= []
	queryset                = bank_info.objects.all()
	serializer_class        = BankSerializer
	pagination_class 		= BankAPIViewPagination
	filter_backends 		= [SearchFilter , OrderingFilter,DjangoFilterBackend]
	search_fields			= ['ifsc']
	filterset_fields  		= ['bank_name','city']




class  BankCreateAPIView(generics.CreateAPIView):
	permission_classes 		= []
	authentication_classes 	= []
	queryset                = bank_info.objects.all()
	serializer_class        = BankSerializer



class  BankDetailAPIView(generics.RetrieveAPIView):
	permission_classes 		= []
	authentication_classes 	= []
	queryset                = bank_info.objects.all()
	serializer_class        = BankSerializer



class  BankUpdateAPIView(generics.UpdateAPIView):
	permission_classes 		= []
	authentication_classes 	= []
	queryset                = bank_info.objects.all()
	serializer_class        = BankSerializer


class  BankDeleteAPIView(generics.DestroyAPIView):
	permission_classes 		= []
	authentication_classes 	= []
	queryset                = bank_info.objects.all()
	serializer_class        = BankSerializer





