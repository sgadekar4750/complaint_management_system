from django.db import models
from django.contrib.auth.models import User

class Profiles(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	first_name = models.CharField(max_length=20)
	last_name = models.CharField(max_length=20)
	MALE = 'M'
	FEMALE = 'F'
	GENDER_CHOICES = (
		(MALE, 'Male'),
		(FEMALE, 'Female'),
		)
	gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
	tax_id_number = models.CharField(max_length=10)

	age = models.IntegerField(max_length=3)
	address = models.CharField(max_length=1024)
	area = models.CharField(max_length=512)
	pin = models.IntegerField(max_length=6)
	
	mobile = models.BigIntegerField()
	

	def __unicode__(self):
				return self.user.username

class Complaint(models.Model):
	WATER = 'WATER'
	ELECTRIC = 'ELECTRIC'
	ROAD = 'ROAD'
	SEWAGE = 'SEWAGE'
	WASTE_COLLECTION = 'WASTE_COLLECTION'
	OTHERS = 'OTHERS'
	CLEANING = 'CLEANING'
	

	TYPEOFCOMP_CHOICES = (
		(WATER, 'water'),
		(ELECTRIC, 'electric'),
		(ROAD, 'road'),
		(SEWAGE, 'sewage'),
		(WASTE_COLLECTION, 'waste_collection'),
		(OTHERS, 'others'),
		(CLEANING, 'cleaning'),
		
		)
	type_of_complaint = models.CharField(max_length=30,
									choices=TYPEOFCOMP_CHOICES,
									default=OTHERS)
	import uuid
	uuid = models.UUIDField(default=uuid.uuid4, unique=True, db_index=True, editable=False)
	
	SOLVED='SOLVED'
	UNSOLVED='NOT SOLVED'
	CON = 'UNDER CONSIDERATION'
	SOLVED_CHOICES = (
		(SOLVED, 'solved'),
		(UNSOLVED, 'unsolved'),
		(CON, 'under consideration')
		)
	solved = models.CharField(max_length=50,
							choices=SOLVED_CHOICES,
							default=UNSOLVED)

	A_ZONE = 'A_ZONE'
	B_ZONE = 'B_ZONE'
	C_ZONE = 'C_ZONE'
	D_ZONE = 'D_ZONE'
	
	

	ZONE_CHOICES = (
		(A_ZONE, 'a_zone'),
		(B_ZONE, 'b_zone'),
		(C_ZONE, 'c_zone'),
		(D_ZONE, 'd_zone'),
		
		)
	sub_muncipal_division = models.CharField(max_length=20,
								choices=ZONE_CHOICES)
	user = models.ForeignKey(User,related_name='topic_content_type1')
	date_created = models.DateTimeField(auto_now_add=True, null=True)




	
	area = models.CharField(max_length=20)
	complaint_desc = models.TextField()
	address = models.CharField(max_length=20)
	

	

	def __unicode__(self):
		return str(self.uuid)



class Employee(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	contact_no = models.CharField(max_length=50)
	zone  = models.CharField(max_length=50)
	work_type = models.CharField(max_length=50)
	
	def __unicode__(self):
		return str(self.id)

