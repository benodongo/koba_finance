from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, IntegerField
from django.db.models.fields.related import ForeignKey
from borrowers.models import Borrower
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class LoanProduct(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class RepaymentCycle(models.Model):
    name = CharField(max_length=200)
    days =IntegerField()

    def __str__(self):
        return self.name

class GuarantorRelationShip(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name



class Loan(models.Model):
    loan_product = models.ForeignKey(LoanProduct, on_delete=models.RESTRICT)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    loan_ref = models.CharField(max_length=200)
    means_choices = [('1','Cash'),('2', 'Cheque'),('3','Mpesa'),('4','EFT')]
    means_disbursed= models.CharField(choices=means_choices,max_length=1, default=None)
    principal_amount = models.DecimalField(max_digits=9 , decimal_places=2)
    loan_release_date = models.DateTimeField()
    interest_choices= [('1','Flat Rate')]
    interest_method = models.CharField(choices=interest_choices, max_length=1 ,default=None)
    interest_type_choices = [('1','Percentage Based'),('2','Fixed amount per cycle'),]
    interest_type = models.CharField(choices=interest_type_choices, max_length=1 , default=None)
    loan_interest =models.DecimalField(max_digits=5, decimal_places=2)
    rate_period = [('1','Per Day'), ('2','Per Week'),('3','2 weeks'),('4','Monthly')]
    rate_cycle = models.CharField(choices=rate_period , max_length=1, default=None)
    duration_choices = [('1','Day(s)'),('2','Week(s)'),('3','Month(s)'),('4','Year(s)')]
    loan_duration = models.IntegerField()
    repayment_cycle = models.ForeignKey(RepaymentCycle, on_delete=models.CASCADE)
    number_of_repayments = models.IntegerField()
    loan_application_fee = models.DecimalField(max_digits=6 , decimal_places=2)
    status_choices = [('1','Initiated'),('2','Pending Approval'),('3','Approved'),('4','Disbursed')]
    loan_status = models.CharField(choices=status_choices, max_length=1 , default='1')

    def __str__(self):
        return self.loan_ref


class Guarantor(models.Model):
    first_name = models.CharField(max_length=200)
    other_names = models.CharField(max_length=200)
    id_number = models.CharField(max_length=200)
    kra_pin = models.CharField(max_length=200)
    phone_number = models,CharField(max_length=200)
    relationship = models.ForeignKey(GuarantorRelationShip, on_delete=models.CASCADE)
    loan = models.ForeignKey(Loan , on_delete=models.RESTRICT)

    def __str__(self):
        return self.first_name


class LoanApproval(models.Model):
    loan = models.OneToOneField(Loan, default=None, null=True , on_delete=models.CASCADE)
    remarks = models.TextField()
    documents_confirmation = models.BooleanField(blank=True)
    credit_score_check = models.BooleanField(blank=True)
    status_choices = [('1','Approve'),('2','Reject')]
    status = models.CharField(choices=status_choices, max_length=1)
    approved_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_approved = models.DateTimeField(default=datetime.now, blank=True)


class LoanRepayment(models.Model):
    loan = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    means_choices = [('1','Cash'),('2', 'Cheque'),('3','Mpesa'),('4','EFT')]
    payment_method = models.CharField(choices=means_choices, max_length=1)
    amount = models.DecimalField(max_digits=9 , decimal_places=2)
    date_collected = models.DateTimeField()
    collected_by = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    date_modified = models.DateTimeField(default=datetime.now, blank=True)

class BorrowerSMS(models.Model):
    borrower = models.ForeignKey(Borrower,default=None, on_delete=models.CASCADE)
    phone =  models.CharField(max_length=20)
    loan = models.ForeignKey(Loan, default=None , on_delete=models.CASCADE)
    message = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.borrower