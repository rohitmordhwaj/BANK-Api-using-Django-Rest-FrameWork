from rest_framework import serializers
#from bank.models import bank_info


class BankSerializer(serializers.Serializer):

	ifsc    		= serializers.CharField()
	bank_id        	= serializers.IntegerField()   
	branch   		= serializers.CharField()
	address  		= serializers.CharField()
	city			= serializers.CharField()
	district 		= serializers.CharField()
	state			= serializers.CharField()
	bank_name  		= serializers.CharField()




