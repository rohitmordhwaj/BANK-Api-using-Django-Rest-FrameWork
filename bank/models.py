from django.db import models

# Create your models here.


class bank_info(models.Model):
	ifsc    		= models.TextField(max_length=200 , primary_key=True)
	bank_id        	= models.IntegerField()   
	branch   		= models.CharField(max_length=30000)
	address  		= models.TextField(max_length= 100000)
	city			= models.CharField(max_length=5000)
	district 		= models.CharField(max_length=5000)
	state			= models.CharField(max_length=20000)
	bank_name  		=models.CharField(max_length=20000)


	def __str__ (self):
		return self.bank_name