import datetime
from django.utils.timezone import now
from django.db import models
from django.utils import timezone

# Create your models here.

class Product(models.Model):
	name = models.CharField("Product Name", max_length=30)
	cost = models.IntegerField("Cost per Kg", default=0)
	wages = models.DecimalField(max_digits=5, decimal_places=3) # wages per Kg
	weight = models.DecimalField(max_digits=7, decimal_places=3) # weight of the products in kg

	def is_available(self, w): # use for reduce_product 
		return ((self.weight - w) >= 0)

	def reduce_product(self, w): # use for customer delivery  
		if(self.is_available(w)):
			self.weight -= w
			self.save()
		else:
			print("There is less or no Product {}".format(self.name)) 
			return

	def add_product(self, w): # Employee add products 
		self.weight += w
		self.save()

	def __str__(self):
		return self.name 

class Salary(models.Model):
	amount = models.DecimalField(max_digits=7, decimal_places=2)
	
	date = models.DateTimeField('date of salary updated')

class Employee(models.Model):
	name = models.CharField("Employee Name", max_length=30, default='NULL', blank=True)
	designation = models.CharField("Designation", max_length=30, default='Nothing', blank=True)
	address = models.CharField(max_length=70, default='Not Found', blank=True)
	phone = models.CharField("Phone Number", max_length=11, default='0000000', blank=True)
	dob = models.DateTimeField('date of birth', default=now, blank=True)
	doj = models.DateTimeField('date of Joined', default=now, blank=True)
	salary = models.DecimalField(max_digits=12, decimal_places=2,  default=0.0, blank=True)
	
	#bonus = models.DecimalField(max_digits=7, decimal_places=2)

	#paid_status = models.BooleanField(default=False)

	#product = models.ManyToManyField(Product)

	GENDER_MALE = 0
	GENDER_FEMALE = 1
	GENDER_OTHERS = 2
	GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female'), (GENDER_FEMALE, 'Others') ]
	gender = models.IntegerField(choices=GENDER_CHOICES, default=2)

	def __str__(self):
		return self.name ; 

	def update_work(self, weight):
		self.product.add_product(weight)
		self.salary.add_amount(weight * product.wage)
		self.save()

	def add_bonus(self, amt):
		self.bonus += amt 
		self.save()
