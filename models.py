from django.db import models

# Create your models here.
class Destination(models.Model):
	location1=models.CharField(max_length=50)
	location2=models.CharField(max_length=50)
	flight_name=models.CharField(max_length=50)
	price=models.IntegerField()
	date=models.DateField()


class booking(models.Model):
	Passport=models.CharField(max_length=20)
	date1=models.DateField()
	locality=models.CharField(max_length=50)
	city=models.CharField(max_length=20)
	ps=models.CharField(max_length=20)
	pin=models.IntegerField()
	state=models.CharField(max_length=20)
	flightid=models.CharField(max_length=20)
	boarding=models.CharField(max_length=30)
	date2=models.DateField()
	tickets=models.IntegerField()
	classs=models.CharField(max_length=50)


	
		