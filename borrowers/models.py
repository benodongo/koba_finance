from os import name, truncate
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

from django.db.models.deletion import CASCADE

class Borrower(models.Model):
   first_name = models.CharField(max_length=200)
   other_name = models.CharField(max_length=300)
   business_name = models.CharField(max_length=200, blank=True)
   reference = models.CharField(max_length=200)
   Gender_choices = [(1, 'Female'), (2 ,'Male'),]
   gender = models.IntegerField(choices=Gender_choices, default=1)
   title_choices = [(1, 'Mr'),(2, 'Mrs'), (3, 'Miss'),]
   title = models.IntegerField(choices= title_choices, default=None)
   mobile = models.CharField(max_length=20)
   email = models.CharField(max_length=20)
   nationality = models.CharField(max_length=200)
   marital_choices = [('1','Single'),('2','Married'),('3','Divorced'),('4','Widowed')]
   marital_status = models.CharField(choices=marital_choices, max_length=1,  default=None)
   dob = models.DateTimeField(blank=True)
   id_number = models.CharField(max_length=200, blank=True)
   id_upload = models.FileField(upload_to = 'borrower_files/%Y/%m%d/',blank=True)
   kra_pin = models.CharField(max_length=200, blank=True)
   pin_upload = models.FileField(upload_to = 'borrower_files/%Y/%m%d/',blank=True)
   number_of_children = models.IntegerField(blank=True)
   number_of_dependants = models.IntegerField(blank=True)
   credit_score = models.DecimalField(max_digits=5, decimal_places=2)
   borrower_photo = models.ImageField(upload_to='photos/%Y/%m%d/')
   description = models.TextField(blank=True)
   borrower_files = models.FileField(upload_to = 'borrower_files/%Y/%m%d/',blank=True)
   modified_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
   date_modified = models.DateTimeField(default=datetime.now, blank=True)

   def __str__(self):
       return self.first_name

class Bank(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)

    def __str__(self):
        return self.name
class BankBranch(models.Model):
    name= models.CharField(max_length=200)
    code = models.CharField(max_length=200)
    bank = models.ForeignKey(Bank , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class BorrowerBank(models.Model):
    borrower = models.OneToOneField(Borrower, default=None, null=True , on_delete=models.CASCADE)
    account_name = models.CharField(max_length=200)
    bank = models.ForeignKey(Bank , on_delete=models.CASCADE)
    bank_branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=200)
    eft = models.CharField(max_length=200)
    mpesa_number = models.CharField(max_length=200 ,blank=True)

    def __str__(self) -> str:
        return self.account_name


class BorrowerCompany(models.Model):
    borrower = models.OneToOneField(Borrower, default=None, null=True , on_delete=models.CASCADE)
    company_name= models.CharField(max_length=200)
    year_of_registration = models.DateTimeField(blank=True)
    registration_number = models.CharField(max_length=200)
    lincense_number = models.CharField(max_length=200)
    number_of_employees = models.IntegerField(blank=True)
    business_lincense =  models.FileField(upload_to = 'borrower_files/%Y/%m%d/',blank=True)
    certificate_of_incorporation =  models.FileField(upload_to = 'borrower_files/%Y/%m%d/',blank=True)
    kra_pin = models.CharField(max_length=200)
    business_pin =  models.FileField(upload_to = 'borrower_files/%Y/%m%d/',blank=True)
    nature_of_business = models.TextField(blank=True)

    def __str__(self):
        return self.company_name

class County(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
class SubCounty(models.Model):
    name = models.CharField(max_length=200)
    county = models.ForeignKey(County, default=None , null=True , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Ward(models.Model):
    name = models.CharField(max_length=200)
    sub_county = models.ForeignKey(SubCounty, default=None , null=True , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class BorrowerContact(models.Model):
    borrower =  models.OneToOneField(Borrower, default=None, null=True , on_delete=models.CASCADE)    
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    alt_phone = models.CharField(max_length=200)
    postal_address = models.CharField(max_length=200, blank=True)
    postal_code = models.CharField(max_length=200 , blank=True)
    postal_city = models.CharField(max_length=200, blank=True)
    county = models.ForeignKey(County , on_delete=models.CASCADE)
    sub_county  = models.ForeignKey(SubCounty, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    nearest_landmark = models.CharField(max_length=200, blank=True)
    family_surname = models.CharField(max_length=200, blank=True)
    name_of_chief = models.CharField(max_length=200, blank=True)
    name_of_ass_chief = models.CharField(max_length=200, blank=True)
    road_street = models.CharField(max_length=200, blank=True)
    estate = models.CharField(max_length=200, blank=True)
    building_plot = models.CharField(max_length=200, blank=True)
    house_office_no = models.CharField(max_length=200, blank=True)
    rental_choices =[('1','Rented'),('2','Owned')]
    Residence_Ownership = models.CharField(choices=rental_choices,max_length=1,  default=None)
    landlord_name = models.CharField(max_length=200, blank=True)
    caretaker_agent_name = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.email

class BorrowerKin(models.Model):
    borrower = models.OneToOneField(Borrower, default=None, null=True , on_delete=models.CASCADE)    
    first_name = models.CharField(max_length=200, blank=True)
    othernames = models.CharField(max_length=200, blank=True)
    relation_choices = [('1','Mother'),('2','Father'),('3','Brother'),('4','Sister'),('5','Relative'),('6','Friend'),('7','Guardian'),('8','Wife'),('9','Husband'),('10','Employer')]
    relationship = models.CharField(choices=relation_choices,max_length=2,  default=None)
    id_number = models.CharField(max_length=200, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=200, blank=True)

    def __str__(self) -> str:
        return self.first_name



class BorrowersGroup(models.Model):
    name = models.CharField(max_length=200)
    group_leader = models.ForeignKey(Borrower, default=None, on_delete=models.CASCADE)
    collector_name= models.CharField(max_length=200 , blank=True)
    meeting_schedule = models.CharField(max_length=200 , blank=True)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name

class GroupMembers(models.Model):
    group = models.ForeignKey(BorrowersGroup , default=None, on_delete=models.CASCADE)
    borrower = models.ForeignKey(Borrower , default=None , on_delete=models.CASCADE)
